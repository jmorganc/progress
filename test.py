#!/usr/bin/python


import sys
import datetime
import time


def main():
    # Weeks
    # TIME_FULL_WEEKS = 40

    # time_full_months = TIME_FULL_WEEKS / 4.0
    # time_full_days = TIME_FULL_WEEKS * 7
    # time_full_hours = time_full_days * 24
    # time_full_minutes = time_full_hours * 60
    # time_full_seconds = time_full_minutes * 60

    # print 'Months: {0}\nWeeks: {1}\nDays: {2}\nHours: {3}\nMinutes: {4}\nSeconds: {5}\n'.format(time_full_months, TIME_FULL_WEEKS, time_full_days, time_full_hours, time_full_minutes, time_full_seconds)

    DT_0 = datetime.datetime(2014, 9, 22, 12)
    dt_0_ts = time.mktime(DT_0.timetuple())

    #now_str = datetime.datetime.now().strftime('%Y-%m-%d')
    now = datetime.datetime.now()
    now = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    now_ts = time.mktime(now.timetuple())

    full_term = DT_0 + datetime.timedelta(weeks=40)
    full_term_ts = time.mktime(full_term.timetuple())

    print dt_0_ts, DT_0
    print now_ts, now
    print full_term_ts, full_term


if __name__ == '__main__':
    sys.exit(main())
