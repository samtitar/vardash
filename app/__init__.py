from flask import Flask

app = Flask(__name__)

from app import views

if __name__ == "main":
    app.run()