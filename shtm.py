#! /usr/bin/env python
# compose the links

import string, time

from settings import cache

def compose(SrcGroup, DestNewsGroups, DestName):
	summary = file( cache() + SrcGroup + '.sum', 'r').read()
	if len(summary) == 0 : 
		records = ""
	else: 
		records = ""
		for record in string.split(summary, chr(30)):
			fields = string.split(record, chr(31))
			records += '\n\n<p><h3>' + fields.pop(0) + '</h3>\n'
			for url in fields:
				line = '<li><a href="%s">%s</a></li>\n' % ( url, url)
				records += line 

	file( cache() + DestName, 'w').write(records)

def trycompose(SrcGroup, DestNewsGroups, DestName):
	compose(SrcGroup, DestNewsGroups, DestName)
	#except:

def batch():
	trycompose('alt.comp.freeware', 'alt.comp.freeware', 'alt.comp.freeware.shtm')
	trycompose('alt.comp.freeware.games', 'alt.comp.freeware.games', 'alt.comp.freeware.games.shtm')
	trycompose('alt.comp.freeware.games', 'alt.comp.freeware, alt.comp.freeware.games', 'both.shtm')

if __name__ == '__main__':
	batch()
