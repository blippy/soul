#! /usr/bin/env python

#SOUL - Summary Of Usenet Links
#Author: Mark Carter
#This file is released into the public domain
#Started 06-May-2004



#--------------------------------------------------------------------------#

import glob, re
import  string
from os.path import basename

import settings


#--------------------------------------------------------------------------#

def UniqSortedList(l):
    s = set(l)
    result = list(s)    
    def cmpfunc(a,b): return cmp(string.lower(a) , string.lower(b))
    result.sort(cmpfunc)
    return result

#--------------------------------------------------------------------------#

def SimplifyMessage(msg):
    header, body = string.split(msg , "\n\n" ,1)

    #eliminate the signature
    try: 
        sections = re.split("\n--\s*\n", body,1)
        main = sections[0]
    except ValueError: 
        main = body
        
    #eliminate lines beginning with ">"
    NewText = ""
    for line in string.split(main, "\n"):
        if  not re.compile("^>").search(line): NewText += line + "\n"

    #ignore articles containing the text SOUL-OMIT-ARTICLE
    if re.compile("^SOUL-OMIT-ARTICLE", re.MULTILINE).search(NewText):
        NewText = ""
    
    return NewText    

#--------------------------------------------------------------------------#

def StandardiseUrls(urls):
    "Ensure that all the urls are preceeded by http:"
    result = []
    for url in urls:
        if url[:3] == 'www': url = 'http://' + url
        result.append(url)
    return result

#--------------------------------------------------------------------------#

def SummariseArticles(ArticleFileNames):
    subjects = {}
    for article in ArticleFileNames:
	article = file(article, "r").read()
        subject = re.compile('(Subject: +)(.+)').search(article).group(2)
        subject = subject.replace("Re: ","")
        
        r = re.compile('(?:http:|www)[^ \t\n\r\f\v<>\*\(\)]+')
        urls= r.findall(SimplifyMessage(article))
        if len(urls) > 0:
            urls = StandardiseUrls(urls)
            try: subjects[subject] += urls
            except KeyError: subjects[subject] = urls
            
    return subjects

#--------------------------------------------------------------------------#
            
def SummariseA(digest):
	"Produce a summary categorised by subject"
	SubjectKeys = UniqSortedList(digest.keys())
	summary = []
 	for subject in SubjectKeys:
        	urls = UniqSortedList(digest[subject])
        	summary.append(subject  + chr(31) + string.join(urls, chr(31)))
        
	return string.join(summary,chr(30)) # I use 30 for a record separator, 31 for a field separator

#--------------------------------------------------------------------------#

def main(newsgroup):
	articles = []
	lines = file(settings.cache() + newsgroup + ".flt","r").readlines()
	lines = [ string.strip(line) for line in lines ]
	for i in range( (len(lines)+1)/4):
		ArticleFileName = lines[i*4]
		accept = lines[i*4+2]
		if len(ArticleFileName) == 0 or accept != "Accepted": continue
		articles.append(ArticleFileName)

	digest = SummariseArticles(articles)
	summary = SummariseA(digest)
	file(settings.cache() + newsgroup + ".sum", "w").write(summary)

#--------------------------------------------------------------------------#

if __name__ == "__main__":
	main('alt.comp.freeware')
	main('alt.comp.freeware.games')

