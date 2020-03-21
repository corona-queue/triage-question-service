#/bin/bash
source venv/bin/activate
pip install -r requirements.txt
gunicorn --bind '127.0.0.1:8812' app:app

