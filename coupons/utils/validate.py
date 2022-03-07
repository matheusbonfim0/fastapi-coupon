import datetime

from domain.coupon.entities import Coupon

def date_format(date: str) -> bool:
    try: 
        datetime.datetime.strftime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def expiry_date_greater_than_current_date(user_input: Coupon) -> bool:
    try: 
        user_input.expiration < datetime 
        return True
    except Exception:
        return False