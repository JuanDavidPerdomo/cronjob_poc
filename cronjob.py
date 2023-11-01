from datetime import datetime, timedelta
import pytz
import os

utc_time = datetime.now()

col_timezone = pytz.timezone("America/Bogota")

correction_factor = timedelta(hours= 5)
col_time = utc_time - correction_factor

with open('myTimeLog', 'a') as file:
    file.write(f'Hora UTC: {utc_time}\n')
    file.write(f'Hora COL: {col_time}\n')

