from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>ТЗ на FastAPI + WebSocket</title>
       <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <style>
            body {
              background-color: lightblue;
            }
            ul {
                width: 20%;
                margin: center;
                font-family: 'Times New Roman', Times, serif;
                font-style: italic;
            }
        </style>
    </head>
    <body>
        <div class"background-color"></div>
        
        <h1 align="center">Веб страница на fastAPI + WebSocket</h1>
        <center><form action="" onsubmit="sendMessage(event)">
            <p><b><i>Введите сообщение для отправки:</i></b></p>
            <input type="text" id="messageText" autocomplete="off"/>
            <p><p><button type="button" class="btn btn-success">Отправить сообщение</button></p></p>
        </form></center>
        <ul class="mx-auto" id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    message_number = 1
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"{message_number}) Текст введенного сообщения: {data}")
        message_number += 1
