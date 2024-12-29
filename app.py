from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('sitio/index.html')


@app.route('/libros')
def libros():
    return render_template('sitio/libros.html')


@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')


if __name__ == '__main__':
    app.run(debug=True)
