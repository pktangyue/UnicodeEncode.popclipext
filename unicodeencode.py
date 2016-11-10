#!/usr/bin/python
#encoding: utf-8
import os
import sys

try:
    text = os.environ['POPCLIP_TEXT'].decode('utf-8')

    ret = ''
    for char in text:
        ret += '\u%x' % ord(char)

    sys.stdout.write(ret)
    sys.stdout.flush()
except Exception, e:
    print e
