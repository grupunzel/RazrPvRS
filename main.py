from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from controllers import router
from service import device_service
app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}

app = FastAPI(
    title="Smart Home API",
    description="REST API для управления устройствами умного дома",
    version="1.0.0",
)

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def root():
    devices = device_service.read_all()
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
        <table>
          <tr><th>ID</th><th>Название</th><th>Тип</th>
              <th>Комната</th><th>Вкл</th><th>Значение</th></tr>
          {rows}
        </table>
      </body>
    </html>
    """