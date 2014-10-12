#!/usr/bin/env python

import os
import sys

from dropbox import client
from dropbox_config import APP_KEY, APP_SECRET, ACCESS_TYPE
from dropbox_cli import StoredSession

sess = StoredSession(APP_KEY, APP_SECRET, access_type=ACCESS_TYPE)
api_client = client.DropboxClient(sess)
sess.load_creds()

def put_file(path):
    from_file = open(os.path.expanduser(path), 'rb')
    api_client.put_file('/' + os.path.basename(path), from_file)
    print path

if not sess.is_linked():
    print 'Please run dropbox_cli.py and login first'
else:
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print 'puting %s' % filename
        put_file(sys.argv[1])
    else:
        print 'no file to put'
        
