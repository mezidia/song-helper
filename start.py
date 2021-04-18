"""
Main script that launch the programm
"""
import os

def start_bot():
    """
    Script to launch the bot
    """
    os.system('python bot/bot.py')
    print('Launch the bot')


def start_server():
    """
    Script to launch the server
    """
    os.system('python server/manage.py runserver 0.0.0.0:8000')
    print('Launch the server')


if __name__ == '__main__':
    start_bot()
    start_server()
