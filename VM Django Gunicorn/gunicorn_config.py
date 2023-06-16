fichier : conf/gunicorn_config.py

command = '/home/adminweb/django_env/bin/gunicorn'
pythonpath = '/home/adminweb/ecole'
bind = '192.168.43.130:8000'
workers = 3
