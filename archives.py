#! /usr/bin/env python
# make archives.htm

import os, os.path
import glob
import sets

# import common

from settings import *

dates = []
for fname in glob.glob(www() + 'archives/2*'):
    fname = os.path.basename(fname)
    fname , ext =  os.path.splitext(fname)
    y = fname[0:4]
    m = fname[5:7]
    d = fname[8:]
    dates.append((y,m,d))

# def ymd2yyyymmdd(d): return "%s-%s-%s" % d

def sortdate(a,b): 
	ya, ma, da = a
	ya, ma, da = int(ya), int(ma), int(da)
	yb, mb, db = b
	yb, mb, db = int(yb), int(mb), int(db)
	if ya != yb: return yb - ya
	if ma != mb: return mb - ma
	return da - db


dates.sort(sortdate)


txt = ''
yprev = ''
mprev = ''
mon = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December']
for date in dates:
    y, m, d = date
    if y != yprev:
        txt += "<h1>" + y + "</h1>\n"
        yprev = y
    if m != mprev:
        txt += "\n<p><b>" + mon[int(m)-1] + "</b> : "
        mprev = m
    day = '<a href="archives/%s-%s-%s.htm">%s</a> ' % (y, m, d, d)
    txt += day

html = file('archives.htm').read()
html = html.replace('ARCHIVE-FIELD',txt)
file(www() + 'archives.htm',"w").write(html)


    

