python -m pip install -r requirements.txt
python create_db.py
gunicorn main:app -w 1 --log-file


