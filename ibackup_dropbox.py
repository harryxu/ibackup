#!/usr/bin/env python

import os
import sys
import select

from dropbox import client
from dropbox_config import APP_KEY, APP_SECRET, ACCESS_TYPE
from dropbox_cli import StoredSession

sess = StoredSession(APP_KEY, APP_SECRET, access_type=ACCESS_TYPE)
api_client = client.DropboxClient(sess)
sess.load_creds()

if not sess.is_linked():
    print 'Please run dropbox_cli.py and login first'
else:
    # http://stackoverflow.com/a/3763257/157811
    if select.select([sys.stdin,],[],[],0.0)[0]:
        for line in sys.stdin.read().splitlines():
            if line:
                from_file = open(os.path.expanduser(line), 'rb')
                api_client.put_file('/' + line, from_file)
                print line
    else:
        print "No data"
