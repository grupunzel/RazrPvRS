from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy.orm import Session

import crud
import db_models  # noqa: F401  — регистрирует таблицы в Base.metadata
from config import settings
from controllers import router
from database import Base, engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Автосоздание таблиц при старте (в проде лучше Alembic)
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    description="REST API для управления устройствами умного дома",
    version="2.0.0",
    lifespan=lifespan,
)

app.include_router(router)

Instrumentator().instrument(app).expose(app, endpoint="/metrics")


@app.get("/health", tags=["Monitoring"])
def health():
    return {
        "status": "ok",
        "service": "smart-home-api",
        "version": "2.0.0",
        "env": settings.app_env,
    }


@app.get("/info", tags=["Monitoring"])
def info():
    return {
        "app": "Smart Home API",
        "version": "2.0.0",
        "developer": "Brigada 2",
        "stack": "FastAPI + Python + PostgreSQL",
        "env": settings.app_env,
    }


@app.get("/", response_class=HTMLResponse)
def root(db: Session = Depends(get_db)):
    devices = crud.get_all(db)
    rows = "".join(
        f"<tr><td>{d.id}</td><td>{d.name}</td><td>{d.type}</td>"
        f"<td>{d.room}</td><td>{d.power_on}</td><td>{d.value}</td></tr>"
        for d in devices
    ) or "<tr><td colspan='6'>Устройств пока нет</td></tr>"

    return f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Smart Home</title>
        <style>
          body {{ font-family: Arial; padding: 20px; }}
          table {{ border-collapse: collapse; width: 100%; }}
          th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
          th {{ background: #f0f0f0; }}
        </style>
      </head>
      <body>
        <h1>Устройства умного дома</h1>
        <p>
          <a href="/docs">Swagger UI</a> |
          <a href="/metrics">Prometheus /metrics</a> |
          <a href="/health">/health</a> |
          <a href="/info">/info</a>
        </p>
        <table>
          <tr><th>ID</th><th>Название</th><th>Тип</th>
              <th>Комната</th><th>Вкл</th><th>Значение</th></tr>
          {rows}
        </table>
      </body>
    </html>
    """