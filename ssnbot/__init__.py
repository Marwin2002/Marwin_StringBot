import os
import re
import logging
import logging.config
from dotenv import load_dotenv

load_dotenv(override=True)

pattern = re.compile(r"^.\d+$")

# vars
APP_ID = os.environ.get("APP_ID", "27758016")
API_HASH = os.environ.get("API_HASH", "8d34cfffe27ab461eabbf0091b1a27df")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7944175084:AAFNDr6fIKd4t__0Nj0yrMtrdXe2vY_FrHs")
DB_URL = os.environ.get("DB_URL", "postgresql://neondb_owner:Zoly4UziVwD8@ep-lucky-waterfall-a5xirmyo.us-east-2.aws.neon.tech/neondb?sslmode=require")
OWNER_ID = int(os.environ.get('OWNER_ID', "7224419362"))
MUST_JOIN = os.environ.get("MUST_JOIN", "@The_Architect04")
ADMINS = [
    int(user) if pattern.search(user) else user
    for user in os.environ.get("ADMINS", "7224419362").split()
] + [OWNER_ID]


# logging Conf
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
