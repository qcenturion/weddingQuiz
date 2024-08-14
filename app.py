# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Carl and Katelyn's Wedding Quiz</h1>"

if __name__ == '__main__':
    app.run()

# requirements.txt
Flask==2.0.1
gunicorn==20.1.0

# .gitignore
venv/
*.pyc
__pycache__/

# .deployment
[config]
SCM_DO_BUILD_DURING_DEPLOYMENT=true

# startup.txt
gunicorn --bind=0.0.0.0 --timeout 600 app:app
