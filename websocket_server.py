import asyncio     # Импортируем asyncio для работы с асинхронными операциями

import websockets   # Импортируем библиотеку для работы с WebSockets
from websockets import ServerConnection

# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):     # Асинхронно обрабатываем входящие сообщения
    async for message in websocket:
        print(f"Получено сообщение: {message}")     # Логируем полученное сообщение
        response = f"Сервер получил: {message}"     # Формируем ответное сообщение

        for _ in range(5):
            await websocket.send(response) # Отправляем ответ клиенту


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())
