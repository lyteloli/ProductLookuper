from NekoGram.storages.sqlite import SQLiteStorage
from dotenv import load_dotenv
from NekoGram import Neko
from typing import List
import os


load_dotenv()


ADMIN_IDS: List[int] = [int(admin.strip()) for admin in os.getenv('BOT_ADMINS').split(',')]
SEARCH_LIST: List[str] = os.getenv('SEARCH_LIST').replace(', ', ',').split(',')
RUN_INTERVAL: int = int(os.getenv('RUN_INTERVAL', 15)) * 60
STORAGE: SQLiteStorage = SQLiteStorage('persistence/db.db')
NEKO: Neko = Neko(storage=STORAGE, token=os.getenv('BOT_TOKEN'))
