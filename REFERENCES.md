Тема: **Умный дом**. Модель `Device` описывает устройство умного дома.

## Научные статьи

1. *Smart homes and home health monitoring technologies for older adults: A systematic review*
   https://www.sciencedirect.com/science/article/abs/pii/S1386505616300648
   Обосновывает поля `type` (тип устройства: датчик, лампа, термостат), `room` (расположение), `value` (показания датчиков).

2. *A Review of Smart Homes—Past, Present, and Future*
   https://ieeexplore.ieee.org/abstract/document/6177682
   Обосновывает архитектуру «устройство — контроллер — актуатор» и поля `id`, `power_on` (состояние вкл/выкл).

3. *Smart home automation: a literature review*
   https://scholar.google.com/scholar?q=Smart+Home+Automation+A+Literature+Review
   Обосновывает поле `value` (яркость/температура/уставка) и логику обновления (PUT).

4. *A review of smart home applications based on Internet of Things*
   https://www.sciencedirect.com/science/article/abs/pii/S1084804517302801
   Обосновывает `name` (человекочитаемое имя), `created_at` (момент регистрации устройства в системе), CRUD-операции.

5. *Review of Smart-Home Security Using the Internet of Things*
   https://www.mdpi.com/2079-9292/13/16/3343
   Обосновывает необходимость уникального `id`, разграничения по `room` и контроля `power_on` (удалённое управление).

## Логика эндпоинтов

- **POST** — регистрация нового устройства
- **GET** — чтение состояния и показаний
- **PUT** — изменение параметров: включение/выключение, яркость/уставка
- **DELETE** — удаление устройства из системы