from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Текущая дата и время</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-size: 10em;
            background-color: #000000;
            color: #00FF00;
        }
    </style>
</head>
<body>
<div id="current-time"></div>
<script type="text/javascript">
    function updateTime() {
        fetch('/api/time')
            .then(response => response.json())
            .then(data => document.getElementById('current-time').innerText = data.time);
    }

    // Обновляем время каждую секунду
    setInterval(updateTime, 1000);
    updateTime(); // Первоначальное обновление сразу же после загрузки страницы
</script>
</body>
</html>
'''


# API endpoint для получения текущего времени
@app.route('/api/time', methods=['GET'])
def current_time():
    now = datetime.now()
    formatted_time = now.strftime('%d.%m.%Y %H:%M:%S')  # Формат вывода времени
    return jsonify({'time': formatted_time})


if __name__ == '__main__':
    app.run(debug=True)