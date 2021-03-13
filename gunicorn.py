# vim: ft=python

import os
import multiprocessing

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RUNDIR = os.path.join(BASEDIR, 'run')
LOGDIR = os.path.join(BASEDIR, 'log')

bind = '127.0.0.0:18000'
workers =multiprocessing.cpu_count() * 2
chdir = BASEDIR
pythonpath = BASEDIR
daemon = False
pidfile = os.path.join(RUNDIR, 'ocs.pid')

loglevel = 'info'
accesslog = os.path.join(LOGDIR, 'access.log')
errorlog = os.path.join(LOGDIR, 'error.log')
