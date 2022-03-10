import datetime
from datetime import date

def date_format(_date: str) -> bool:
    try: 
        datetime.datetime.strftime(_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def expiry_date_greater_than_current_date(expiration: str) -> bool:
    try: 
        expiration > date.today()
        return True
    except Exception:
        return False