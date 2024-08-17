import os
import logging

logger = logging.getLogger(__name__)


def init_telegram_accounts() -> list[dict]:
    phones = [
        dict(phone=phone.strip())
        for phone in os.getenv('TELEGRAM_ACCOUNTS').split(',')
    ]

    logger.info(f'got telegram accounts: {phones}')
    return phones


TELEGRAM_ACCOUNTS = init_telegram_accounts()
