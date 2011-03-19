#! /usr/bin/env python
# compose emails

import string, time

from settings import cache, load_skel

def compose(SrcGroup, DestNewsGroups, DestName):
	txt = load_skel('email.txt')
	txt = txt.replace('[DEST-GROUP]', DestNewsGroups)
	txt = txt.replace('[SRC-GROUP]', SrcGroup)
	txt = txt.replace('[TIME]', time.asctime())
	summary = file( cache() + SrcGroup + '.sum', 'r').read()
	if len(summary) == 0 : 
		txt = ""
	else: 
		records = ""
		for record in string.split(summary, chr(30)):
			fields = string.split(record, chr(31))
			heading = fields.pop(0)
			records += heading + '\n' + string.join([ "   " + url  for url in fields ], '\n') + '\n\n'

		txt = txt.replace('[SUMMARY]', records)
	file( cache() + DestName, 'w').write(txt)

def trycompose(SrcGroup, DestNewsGroups, DestName):
	compose(SrcGroup, DestNewsGroups, DestName)
	#except:

def batch():
	trycompose('alt.comp.freeware', 'alt.comp.freeware', 'acf.eml')
	trycompose('alt.comp.freeware.games', 'alt.comp.freeware.games', 'acfg.eml')
	trycompose('alt.comp.freeware.games', 'alt.comp.freeware, alt.comp.freeware.games', 'both.eml')

if __name__ == '__main__':
	batch()

