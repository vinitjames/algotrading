from  datetime import datetime
from operator import itemgetter
from typing import Union
import dateparser

import pytz




def format_time(data: Union[int, float, str]) -> float:
    if isinstance(data, (int, float)):
        return data
    if not isinstance(data, str):
        return None
    dt_obj = dateparser.parse(data)
    
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    # if the date is not timezone aware apply UTC timezone
    if dt_obj.tzinfo is None or d_obj.tzinfo.utcoffset(d) is None:
        dt_obj = dt_obj.replace(tzinfo=pytz.utc)
        # return the difference in time
    return int((dt_obj - epoch).total_seconds() * 1000.0)
