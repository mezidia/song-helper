"""
Main script that launch the programm
"""
import os


if __name__ == '__main__':
    os.system('python bot/bot.py & python server/manage.py runserver 0.0.0.0:8000')
