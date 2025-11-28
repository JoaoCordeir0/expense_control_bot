import os
import dotenv 

dotenv.load_dotenv(override=True)

ENV = os.getenv('ENV')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./database.db')