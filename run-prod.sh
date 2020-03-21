#/bin/bash
source venv/bin/activate
pip install -r requirements.txt
gunicorn --bind '0.0.0.0:8812' app:app

