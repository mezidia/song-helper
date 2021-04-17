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
    os.system('python server/manage.py runserver')
    print('Launch the server')


def install_packages():
    """
    Script to install all packages
    """
    print('Install dependencies for bot package')
    os.system('pip install -r bot/requirements.txt')
    print('Install dependencies for server package')
    os.system('pip install -r server/requirements.txt')
    print('Install dependencies for song-helper package')
    os.system('pip install -r song-helper/requirements.txt')


if __name__ == '__main__':
    install_packages()
    start_bot()
    start_server()
