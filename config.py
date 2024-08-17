import os


ACCOUNTS_DIR = "accounts_data"
# TELEGRAM WEB
TELEGRAM_AUTH = dict(
    api_id=os.getenv('TELEGRAM_API_ID'),
    api_hash=os.getenv('TELEGRAM_API_HASH'),
    device_model="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    system_version="Windows",
    app_version="1.57 Z",
    lang_code="en",
    system_lang_code="en-US",
)

DEBUG = True
RETRY_ATTEMPTS = 3

ENABLED_BOTS = [
    'blum',
]

SLEEP_AT_NIGHT = False  # При True ночью фарминг не производится
NIGHT_HOURS = (0, 7)  # Диапазон времени, когда у фермы тихий час
MULTITHREAD = False  # При True на каждый аккаунт будет отдельный поток

try:
    from config_local import *
except ImportError:
    pass
