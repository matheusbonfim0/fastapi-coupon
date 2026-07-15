import datetime
from datetime import date

def date_format(_date: str) -> bool:
    try: 
        datetime.datetime.strptime(_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def expiry_date_greater_than_current_date(expiration: date) -> bool:
    return isinstance(expiration, date) and expiration > date.today()
    
