from lxml import etree
from lxml.html import fromstring, tostring

import cookielib
import mechanize

class XRoxy(object):
    
    def __init__(self):
        self._br = mechanize.Browser()
        
        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        self._br.set_cookiejar(cj)
        
        # Browser options
        self._br.set_handle_equiv(True)
        self._br.set_handle_gzip(True)
        self._br.set_handle_redirect(True)
        self._br.set_handle_referer(True)
        self._br.set_handle_robots(False)
        
        self._br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0')]
        
        
    def fetch_proxies(self, limit_page=5, country='BR', ssl=''):
        for page in xrange(limit_page):
            url = 'http://www.xroxy.com/proxylist.php?port=&type=&ssl=%s&country=%s&latency=&reliability=&sort=reliability&desc=true&pnum=%d#table' % (ssl, country, page)
            
            resp = self._br.open(url)
            
            read = resp.read()
            #print read
            tree = etree.HTML(read)
            table = tree.xpath('/html/body/div[1]/div[2]/table[1]') 
            for tr in tree.xpath("//tr"):
                t = tr.xpath("//td//font[text()='Brand']/following::td[1]")[0]
                print tostring(t)