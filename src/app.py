from flask import Flask, render_template
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    # página inicial
    return render_template('index.html')


@app.route('/about-me')
def about():
    # página sobre mim
    return render_template('about-me.html')


@app.route('/education')
def education():
    # página sobre minha formação acadêmica
    return render_template('education.html')


@app.route('/projects')
def projects():
    # página sobre os projetos que já desenvolvi
    return render_template('projects.html')


@app.route('/navigation')
def navigation():
    # menu de navegação para dispositivos móveis
    return render_template('navigation.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
