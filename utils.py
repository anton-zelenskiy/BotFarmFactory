from os import path, listdir
from importlib import import_module
from config import ENABLED_BOTS

import logging

logger = logging.getLogger(__name__)


def import_bots():
    bots = []
    if path.isdir("bots"):
        for directory in listdir("bots"):
            if directory == 'template':
                continue
            if ENABLED_BOTS and directory not in ENABLED_BOTS:
                continue
            try:
                module = import_module(f"bots.{directory}.client")
                bots.append(module.BotFarmer)
            except ImportError:
                pass
            except Exception as e:
                logger.error(f'import_bots, error occurred: {e}')
    else:
        raise Exception("No bots :(")
    return bots


BOTS = import_bots()
