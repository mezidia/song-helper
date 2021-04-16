import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    """
    Class with the fields for Spotify credentials
    """
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    redirect_uri = os.getenv('REDIRECT_URI')
    username = os.getenv('USERNAME')
