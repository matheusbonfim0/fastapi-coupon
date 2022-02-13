import datetime

def date_format(date: str) -> bool:
    try: 
        datetime.datetime.strftime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False