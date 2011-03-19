#! /usr/bin/env python

#SOUL - Summary Of Usenet Links
#Author: Mark Carter
#This file is released into the public domain
#Started 06-May-2004
# mcarter 26-jun-2006 started major upgrade


# attempts to filter out garbage

#--------------------------------------------------------------------------#

import datetime, glob, os, re,  string

import settings

#--------------------------------------------------------------------------#

class Placeholder:
	def __init__(self, newsgroup):
		self.lastfile = settings.cache() + newsgroup + ".last"

	def load(self):
        	if os.path.exists(self.lastfile):
            		fp =  file(self.lastfile, "r")
		        result = int(fp.readline().split(" ")[0])
            		fp.close()
        	else: result = None
        	return result

	def save(self, ArticleNum):
        	if os.path.exists(self.lastfile):
           		fp = file(self.lastfile, "r")
            		OriginalContents = fp.read()
            		fp.close()
        	else: OriginalContents = ""
        
        	fp = file(self.lastfile, "w")
       		fp.write(str(ArticleNum)+ " " + str(datetime.datetime.now()) + "\n")
        	fp.write(OriginalContents)
        	fp.close()


#--------------------------------------------------------------------------#

def readFilters():
	filters = file("filter").readlines()
	filters = [ string.strip(x) for x in filters]
	filters = [ x for x in filters if len(x) > 0]
	return filters

#--------------------------------------------------------------------------#

def reject(ArticleFileName, filters):
        txt = file(ArticleFileName).read()
        for r in filters:
                m = re.compile(r, re.MULTILINE + re.IGNORECASE).search(txt)
                if m: return r
        return None


#--------------------------------------------------------------------------
def main(newsgroup, filters):
	newsdir = '/uu/news/' + newsgroup.replace(".", "/") + "/"

	# determine what articles are available
	ArticleFileNames = glob.glob( newsdir + '[0-9]*')
	avail = [int(os.path.basename(x)) for x in ArticleFileNames ]
	mavail = max(avail)

	# determine what articles we want to summarise
	p = Placeholder(newsgroup)
	last = p.load()
	if last == None: last = mavail - 10
	articles = [ x for x in ArticleFileNames if int(os.path.basename(x)) > last ]

	# sort the wheat from the chaff
	fpflt = file(settings.cache() + newsgroup + ".flt", "w")
	for article in articles:
		fpflt.write('%s\nNow: %s\n' %(article, str(datetime.datetime.now())))
		m = reject(article, filters)
		if m: fpflt.write( 'Rejected: %s' % (m))
		else: fpflt.write('Accepted')
		fpflt.write('\n%%\n')

	fpflt.close()

	p.save(mavail)

#--------------------------------------------------------------------------#

if __name__ == "__main__":
	filters = readFilters()
	main('alt.comp.freeware', filters)
	main('alt.comp.freeware.games', filters)

