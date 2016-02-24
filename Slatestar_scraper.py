#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      PeterK2
#
# Created:     26/09/2013
# Copyright:   (c) PeterK2 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from BeautifulSoup import BeautifulSoup, Tag, NavigableString
import time
import mechanize, lxml.html
import sys
import re
from mechanize._opener import urlopen
from mechanize._form import ParseResponse

def slateStarText():
    text=''
<<<<<<< HEAD

=======
>>>>>>> 0103651a5fe328ac3d63ebc74ad4cc82870418c3
    sRoot='http://slatestarcodex.com/page/'
    f=open("Slatestar.txt","w")
    #begin loop that goes through list of urls
    for i in range(1,55):
        try:
            print(sRoot+str(i))
            resp=browser.open(sRoot+str(i))
        except Exception:
            print "could not visit "+ str(i)
            print "Unexpected error:", sys.exc_info()[0]
            time.sleep(10)
            continue

        s= resp.read()
        soup=BeautifulSoup(s)

        a=soup.findAll("div",{"class":"pjgm-postcontent"})
        for t in a:
            links= t.findAll('a')
            for link in links:
                link.replaceWith(" %s " % unicode(link.text))
            text=unicode(re.sub('<[^<]+?>', '', unicode(t)))
            f.write(text.encode('utf-8'))

        else:
            continue


    f.close()


browser = mechanize.Browser(factory=mechanize.RobustFactory())
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


#call desired scraper functions
slateStarText()

