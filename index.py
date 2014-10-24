import sys
import bottle
import datetime
import time


@bottle.route('/')
def index():
    return bottle.template('index', test='testtesttest')


bottle.debug(True)
bottle.run(reloader=True)
