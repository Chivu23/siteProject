'''
O aplicatie web, un e-commerce facut pentru exercitiu.
sau pentru exercitii.

'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])       # am implementat o ruta
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=7000)
