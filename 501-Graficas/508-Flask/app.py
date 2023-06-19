from flask import Flask
from flask import request


from bs4 import BeautifulSoup
app = Flask(__name__)

edad = 45

@app.route('/')
def inicio():
    global edad
    edad += 1
    return str(edad)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
