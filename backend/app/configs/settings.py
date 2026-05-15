import os

from dotenv import load_dotenv

load_dotenv()


class ConfigAppFastAPI:
    PROJECT_NAME: str = os.getenv('PROJECT_NAME')
    PROJECT_VERSION: str = os.getenv('PROJECT_VERSION')
    PROJECT_DESCRIPTION: str = os.getenv('PROJECT_DESCRIPTION')
    API_PREFIX: str = os.getenv('API_PREFIX')
