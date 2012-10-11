import urllib
import urllib2

# urllib2 example 2
GOODREADS = "http://www.goodreads.com/author/list"
GOODREADS_KEY = "FCeXl2vCxU22dmoVkGub4A"
ALICE_MUNRO_ID = 6410

params = {
    "key": GOODREADS_KEY,
    "id":  ALICE_MUNRO_ID,
    }

encoded_args = urllib.urlencode(params)
URI = GOODREADS + "?" + encoded_args
req = urllib2.Request(URI)
response = urllib2.urlopen(req)
print response
#print response.read()
