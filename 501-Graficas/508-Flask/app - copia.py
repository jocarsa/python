from flask import Flask
from flask import request


from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/')
def inicio():
    return "Hola"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
