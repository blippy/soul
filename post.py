#! /usr/bin/env python

import logging, nntplib, os, os.path, time, StringIO, traceback

import settings
    
def email(f):
    	"email the summary to an appropriate group"
    	server = nntplib.NNTP(settings.host())
    	server.post(f)
    	server.quit()


def tryemail(eml):
	MsgFile = settings.cache() + eml
	try:
		if os.path.getsize(MsgFile) >0:
			f = open(MsgFile)
			email(f)
			f.close()
	except os.error: pass

def main():
	tryemail('acf.eml')
	tryemail('acfg.eml')
        
if __name__ == "__main__":
	main()
    
