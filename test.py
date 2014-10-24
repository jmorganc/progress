#!/usr/bin/python


import datetime


# Weeks
# TIME_FULL_WEEKS = 40

# time_full_months = TIME_FULL_WEEKS / 4.0
# time_full_days = TIME_FULL_WEEKS * 7
# time_full_hours = time_full_days * 24
# time_full_minutes = time_full_hours * 60
# time_full_seconds = time_full_minutes * 60

# print 'Months: {0}\nWeeks: {1}\nDays: {2}\nHours: {3}\nMinutes: {4}\nSeconds: {5}\n'.format(time_full_months, TIME_FULL_WEEKS, time_full_days, time_full_hours, time_full_minutes, time_full_seconds)

DT_0 = datetime.datetime(2014, 9, 22, 12)
#now_str = datetime.datetime.now().strftime('%Y-%m-%d')
now = datetime.datetime.now()
now = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
full_term = DT_0 + datetime.timedelta(weeks=40)

print type(DT_0), DT_0
print type(now), now
print type(full_term), full_term