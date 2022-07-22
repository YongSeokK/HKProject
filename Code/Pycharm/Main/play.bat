@echo off

cd C:/G_Project/Code/Pycharm/Main

set FLASK_APP=server
set FLASK_ENV=development

flask run --port 8000