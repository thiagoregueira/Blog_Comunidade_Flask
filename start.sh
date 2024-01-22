python -m pip install -r requirements.txt
gunicorn main:app -w 1 --log-file


