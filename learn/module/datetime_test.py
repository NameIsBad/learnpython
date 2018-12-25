# from datetime import datetime,timedelta
# print(datetime.now(tz=None))

# print(datetime(2018,8,6,17,38,55))

# now = datetime.now()
# print(now.timestamp())

# t = 1533548407.439171
# print(datetime.fromtimestamp(t))

# cday = datetime.strptime('2015-8-8 12:1:1', '%Y-%m-%d %H:%M:%S')
# print(cday)

# now = datetime.now()
# print(now + timedelta(days = 1))
# print(now - timedelta(days = 1))

import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    return datetime.timestamp(dt,tz_str)
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')