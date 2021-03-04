"""
Main script that launch the programm
"""
import os

def start_bot():
    """
    Script to launch the bot
    """
    os.system('pip install -r bot/requirements.txt')
    print('Install dependencies for bot package')
    os.system('python bot/bot.py')
    print('Launch the bot')


def start_server():
    """
    Script to launch the server
    """
    os.system('pip install -r server/requirements.txt')
    print('Install dependencies for server package')
    os.system('python server/manage.py runserver')
    print('Launch the server')


if __name__ == '__main__':
    start_bot()
    start_server()
