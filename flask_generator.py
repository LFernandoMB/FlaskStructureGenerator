import os
import subprocess
import sys

# Estrutura do projeto
project_structure = {
    "application": {
        "static": {
            "css": {
                "style.css": """
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    text-align: center;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-bottom: 20px;
}

p {
    margin-top: 20px;
    text-align: center;
    color: black;
}

a {
    text-align: center;
    color: white;
}

.btn {
    text-align: center;
    display: inline-block;
    width: 150px;
    height: 30px;
    margin: 5 10px;
    border-radius: 5px;
    text-decoration: none;
}

.btn.red {
    background-color: red;
}
"""
            },
            "images": {}
        },
        "templates": {
            "layout.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}WTF{% endblock %}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h1>{% block header %}Título Geral{% endblock %}</h1>
        <div class="buttons">
            <a href="/" class="btn red">Botão</a>
        </div>
        <div>
            {% block content %}{% endblock %}
        </div>
    </div>
</body>
</html>
""",
            "index.html": """
{% extends "layout.html" %}

{% block title %}WTF{% endblock %}

{% block header %}Página 1{% endblock %}

{% block content %}
<p>Bem-vindo à Página 1!</p>
{% endblock %}
"""
        },
        "__init__.py": """
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from . import routes
""",
        "logger_config.py": """
import logging

def setup_logger(name):
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] - [%(name)s] - [%(levelname)s] - [%(funcName)s] - [%(message)s]',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(name)
    return logger
""",
        "routes.py": """
from flask import render_template
from . import app
from datetime import datetime
from .logger_config import setup_logger

logger = setup_logger(__name__)

@app.route('/')
def index():
    logger.info(f"Página 1 acessada: {datetime.now()}")
    return render_template('index.html')
"""
    },
    "assets": {},
    ".env": 'SECRET_KEY="123e4567-e89b-12d3-a456-426614174000"\n',
    ".gitignore": """
__pycache__/
*.pyc
*.pyo
*.log
.env
env/
venv/
""",
    ".dockerignore": """
__pycache__/
*.pyc
*.pyo
*.log
.env
env/
venv/
""",
    "config.py": """
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
""",
    "Procfile": "web: gunicorn run:app\n",
    "Dockerfile": """
FROM python:

WORKDIR /application

COPY . /application

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
""",
    "requirements.txt": "Flask\ngunicorn\npython-dotenv\n",
    "run.py": """
from application import app

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=3000)
    app.run(debug=True, port=3000)
"""
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)


if __name__ == "__main__":
    project_path = sys.argv[1]
    os.makedirs(project_path, exist_ok=True)
    create_structure(project_path, project_structure)

    commands = [
        ["python", "-m", "venv", "env"],
        [r"env\Scripts\activate.bat &&", "pip", "install", "flask", "gunicorn"],
        [r"env\Scripts\activate.bat &&", "pip", "freeze", ">", "requirements.txt"],
    ]

    print(f"Estrutura do projeto Flask '{project_path}' criada em: {os.path.abspath(project_path)}")
    print("Executando comandos adicionais...")

    for cmd in commands:
        try:
            subprocess.run(" ".join(cmd), cwd=project_path, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o comando: {' '.join(cmd)}\n{e}")
