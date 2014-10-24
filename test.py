#!/usr/bin/python


import sys
import datetime
import time


def main():
    DT_0 = datetime.datetime(2014, 9, 22, 12)
    dt_0_ts = time.mktime(DT_0.timetuple())

    now = datetime.datetime.now()
    now = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    now_ts = time.mktime(now.timetuple())

    full_term = DT_0 + datetime.timedelta(weeks=40)
    full_term_ts = time.mktime(full_term.timetuple())

    start_end_ts = (dt_0_ts, full_term_ts)

    now_pct = get_percent(start_end_ts, now_ts)
    print 'Current percent: {0}'.format(now_pct)
    width_px = 500
    print 'Pixels: 0 to {0}: {1}'.format(width_px, get_percent_pixels(width_px, now_pct))


def get_percent(start_end_ts, now_ts):
    return (now_ts - start_end_ts[0])/(start_end_ts[1] - start_end_ts[0]) * 100


def get_percent_pixels(width_px, now_pct):
    return (now_pct * width_px / 100.0)


if __name__ == '__main__':
    sys.exit(main())
