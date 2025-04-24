from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def now_time():
    current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    return f"""
        <html>
            <head>
                <title>Текущая дата и время</title>
            </head>
            <body style="display: flex; justify-content: center; height: 100vh; margin: 0;">
                <div style="text-align: center;">
                    <h1>{current_time}</h1>
                </div>
            </body>
        </html>
        """

if __name__ == "__main__":
    app.run(debug=True)