import datetime
import pandas_market_calendars as mcal
from typing import List, Optional, Tuple
from dateutil.relativedelta import relativedelta


def get_trading_days_ytd(
    less_today: bool = True,
    format_dates: bool = True,
    exchange: str = 'NYSE'
) -> List[str]:
    
    """
    docs
    """

    trading_calendar = mcal.get_calendar(exchange)
    
    current_year = datetime.datetime.now().year
    start_date = f'{current_year}-01-01'
    end_date = None

    if less_today:
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        end_date = yesterday.strftime('%Y-%m-%d')
    else:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    trading_days = trading_calendar.valid_days(
        start_date=start_date,
        end_date=end_date
    )

    if format_dates:
        return [day.strftime('%Y-%m-%d') for day in trading_days]
    else:
        return trading_days
    

#######################################################
#######################################################


def get_trading_days_range(
    start_date: str,
    end_date: str,
    format_dates: bool = True,
    exchange: str = 'NYSE'
) -> List[str]:
    
    """
    docs
    """

    trading_calendar = mcal.get_calendar(exchange)
    
    trading_days = trading_calendar.valid_days(
        start_date=start_date,
        end_date=end_date
    )
    

    if format_dates:
        return [day.strftime('%Y-%m-%d') for day in trading_days]
    else:
        return trading_days


#######################################################
#######################################################


def format_date(date: datetime.date) -> str:
    
    """
    docs
    """
    
    return date.strftime('%Y-%m-%d')


#######################################################
#######################################################

def today(format_date: bool = False) -> str:
    
    """
    docs
    """
    
    if format_date:
        return datetime.datetime.now().strftime('%Y-%m-%d')
    else:
        return datetime.datetime.now()
    

#######################################################
#######################################################


def yesterday(format_date: bool = False) -> str:
    
    """
    docs
    """
    
    yesterday_date = today() - datetime.timedelta(days=1)
    
    if format_date:
        return yesterday_date.strftime('%Y-%m-%d')
    else:
        return yesterday_date


#######################################################
#######################################################


def get_5year_ago_date() -> str:
    
    """
    docs
    """

    today = datetime.datetime.now()
    five_years_ago = today - relativedelta(years=5)
    result = five_years_ago + datetime.timedelta(days=1)
    return result.strftime('%Y-%m-%d')


#######################################################
#######################################################


def string_formating(number: int) -> str:
    
    """
    docs
    """

    if number < 10:
        return f"0{number}"
    else:
        return str(number)