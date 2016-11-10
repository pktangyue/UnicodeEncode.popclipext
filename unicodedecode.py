#!/usr/bin/python
#encoding: utf-8
import os
import sys

try:
    text = os.environ['POPCLIP_TEXT']

    ret = ''
    for char in text.split('\u'):
        if not char:
            continue
        ret += unichr(int(char, 16))

    sys.stdout.write(ret.encode('utf-8'))
    sys.stdout.flush()
except Exception, e:
    print e
