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
def regions():
    # página sobre minha formação acadêmica
    return render_template('education.html')


@app.route('/projects')
def project():
    # página sobre os projetos que já desenvolvi
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
