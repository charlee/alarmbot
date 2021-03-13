# vim: ft=python

import os
import multiprocessing

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RUNDIR = os.path.join(BASEDIR, 'run')
LOGDIR = os.path.join(BASEDIR, 'log')

bind = '127.0.0.1:18000'
workers = 2
chdir = BASEDIR
pythonpath = BASEDIR
daemon = False
pidfile = os.path.join(RUNDIR, 'alarmbot.pid')

loglevel = 'info'
accesslog = os.path.join(LOGDIR, 'access.log')
errorlog = os.path.join(LOGDIR, 'error.log')
