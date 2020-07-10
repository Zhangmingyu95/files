__author__ = 'mingyu.zhang'
import datetime,re
'''now=datetime.datetime.now().timestamp()
d=datetime.datetime(2015,2,4,12,2)
str(now)
print(type(now),type(d))
print(d)
print(now,d.timestamp())
#print(now.timetamp())

print(d.tzinfo)'''

def to_timestamp(dt_str,tz_str):
    dt=datetime.datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    dt_utc=re.match(r'\w*?.?(\d)+\:\d{2}',tz_str)
    dt_utc=int(dt_utc.group(1))
    n=datetime.timezone(datetime.timedelta(hours=dt_utc))
    utc_dt=dt.replace(tzinfo=n)

    return utc_dt.timestamp()

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2