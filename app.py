from flask import Flask

from rest_api_application import app

@app.route('/')
def index():
    return 'ok'

if __name__ == "__main__":
    app.run()