import os
import subprocess
import sys

project_structure = {
    "application": {
        "static": {
            "css": {
                "style.css": """body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    text-align: center;
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 80%;
    max-width: 800px;
}

.logo img {
    width: 100px;
    height: auto;
    margin-bottom: 20px;
}

h1 {
    color: #555;
    margin-bottom: 20px;
}

.image-box img {
    width: 300px;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

footer {
    margin-top: 20px;
    font-size: 0.9em;
    color: #999;
}

"""
            },
            "images": {}
        },
        "templates": {
            "layout.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
""",
            "index.html": """
{% extends "layout.html" %}

{% block title %}Welcome to Flask{% endblock %}

{% block content %}
<div class="container">
    <!-- Logo -->
    <div class="logo">
        <img src="data:image/png;base64,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" alt="Flask Logo">
    </div>
    <!-- Título -->
    <h1>Welcome to Flask Easy Structure</h1>
    <!-- Imagem -->
    <div class="image-box">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" alt="Python Logo">
    </div>
    <!-- Rodapé -->
    <footer>
        <p>Created by Luis Fernando M. Bezerra</p>
    </footer>
</div>
{% endblock %}

"""
        },
        "__init__.py": """from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from . import routes
""",
        "logger_config.py": """import logging

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
        "routes.py": """from flask import render_template
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
    "config.py": """import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
""",
    "Procfile": "web: gunicorn run:app\n",
    "Dockerfile": """FROM python

WORKDIR /application

COPY . /application

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
""",
    "requirements.txt": "Flask\ngunicorn\npython-dotenv\n",
    "run.py": """from application import app

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
        [r"env\Scripts\activate.bat &&", "pip", "install", "flask", "gunicorn", "python-dotenv"],
        [r"env\Scripts\activate.bat &&", "pip", "freeze", ">", "requirements.txt"],
    ]

    print(f"Estrutura do projeto Flask '{project_path}' criada em: {os.path.abspath(project_path)}")
    print("Executando comandos adicionais...")

    for cmd in commands:
        try:
            subprocess.run(" ".join(cmd), cwd=project_path, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o comando: {' '.join(cmd)}\n{e}")
