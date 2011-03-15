#! /usr/bin/env python
# make feed.rss

import os, os.path
import glob
import datetime

from settings import *

dates = []
for fname in glob.glob(www() + 'archives/2*'):
    fname = os.path.basename(fname)
    fname , ext =  os.path.splitext(fname)
    y = fname[0:4]
    m = fname[5:7]
    d = fname[8:]
    dates.append((y,m,d))

def sortfunc(a,b):
    a1 = '%s-%s-%s' % a
    b1 = '%s-%s-%s' % b
    return cmp(b1, a1)
    
dates.sort(sortfunc)

dates = dates[:14] # last 2 weeks

def tagged(tag, content): return "<%s>%s</%s>\n" % (tag, content, tag)

txt = ""
for date in dates:
    y, m, d = date
    datetxt = "%s-%s-%s" % date
    txt += "<item>\n"
    txt += tagged("title" , "Summary for " + datetxt)
    txt += tagged("link",  "http://www.mcleod-schmidt.id.au/~acfsoul/archives/" + datetxt + ".htm")
    txt += tagged("description", "Summary of acf for " + datetxt)
    txt += tagged("pubDate", datetxt)
    txt += "</item>\n"


html = file('feed.rss').read()
html = html.replace('ITEMS-FIELD',txt)

#n = datetime.datetime.now()
#n = n.strftime('%d/%m/%Y %H:%M')
#n = n.stfrtime("%a, %d %b %Y %T %Z")
n = datetime.datetime.now().strftime('%a, %d %b %Y %X +0000')
html = html.replace('PUBDATE-FIELD', n)

file(www() + 'feed.rss',"w").write(html)


    

