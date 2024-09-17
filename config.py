import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')  # Load secret key from .env
    MONGO_URI = os.getenv('MONGO_URI')    # Load MongoDB URI from .env
    MONGO_DBNAME = os.getenv('MONGO_DBNAME')  # Load database name from .env
    PORT=os.getenv('PORT') #Load Port
