TELEGRAM_ACCOUNTS = [
    dict(phone='+995579323517'),
]

try:
    from accounts_local import *
except ImportError:
    pass
