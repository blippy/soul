#! /usr/bin/env python
# make latest.htm

import datetime

from settings import *

html = load_skel('latest.htm')

genfield = str(datetime.datetime.now())
html = html.replace('GEN-FIELD',genfield)

acf = file(cache() + 'alt.comp.freeware.shtm').read()
html = html.replace('ACF-FIELD',acf)

acfg = file(cache() + 'alt.comp.freeware.games.shtm').read()
html = html.replace('ACFG-FIELD',acfg)

file(www() + 'latest.htm',"w").write(html)

n = datetime.date.today()
fname = www() + 'archives/' + str(n) + '.htm'
file(fname,"w").write(html)
