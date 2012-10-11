# urllib2 example 1
import urllib2
import urllib

req = urllib2.Request('http://www.goodreads.com')
response = urllib2.urlopen(req)
goodreads_homepage = response.read()
