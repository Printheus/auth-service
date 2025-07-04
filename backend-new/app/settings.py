from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    VERSION = 1
    PRIVATE_KEY = os.environ.get("PRIVATE_KEY", "./private_key.pem")
    PUBLIC_KEY = os.environ.get("PUBLIC_KEY", "./public_key.pem")
    ACCESS_TOKEN_EXPIRE = 15
    REFRESH_TOKEN_EXPIRE = 24 * 60
    DATABASE = {
        "drivername": "mysql+mysqldb",
        "database": os.environ.get("DATABASE_NAME", "mydb"),
        "username": os.environ.get("DATABASE_USERNAME", "auth"),
        "password": os.environ.get("DATABASE_PASSWORD"),
        "host": os.environ.get("DATABASE_HOST", "127.0.0.1"),
        "port": 3306
    }
    PORT = int(os.environ.get("PORT"))

    @property
    def private_key(self):
        return self.PRIVATE_KEY

    @property
    def public_key(self):
        return self.PUBLIC_KEY


settings = Settings()
