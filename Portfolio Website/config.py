import os
from dotenv import load_dotenv

"""
make .env file with sensitive data in it.
SECRET_KEY = "THIS_IS_noT_SeCRet_LOL"
SQLALCHEMY_DATABASE_URI = "sqlite:///server.db
"""

dotenv_path = ".env"
load_dotenv(dotenv_path)
SECRET_KEY = os.environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")