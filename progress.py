import sys
import bottle
import datetime
import time


DT_0 = datetime.datetime(2014, 9, 22, 12)
dt_0_ts = time.mktime(DT_0.timetuple())

# now = datetime.datetime.now()
# now = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
# #now_ts = time.mktime(now.timetuple())
# now_ts = time.time()

full_term = DT_0 + datetime.timedelta(weeks=40)
full_term_ts = time.mktime(full_term.timetuple())

start_end_ts = (dt_0_ts, full_term_ts)


@bottle.route('/static/<filename>')
def static(filename):
    return bottle.static_file(filename, root='./')


@bottle.route('/get/percent')
def percent():
    now_ts = _now_ts()
    return str(round(((now_ts - start_end_ts[0])/(start_end_ts[1] - start_end_ts[0]) * 100), 5))


@bottle.route('/')
def index():
    return bottle.template('index', test='testtesttest')


def _now_ts():
    return time.time()


bottle.debug(True)
bottle.run(reloader=True, port=8282)
