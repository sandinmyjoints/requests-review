import json
import requests
from oauth_hook import OAuthHook
from urlparse import parse_qs
from local.goodreads import GOODREADS_KEY, GOODREADS_SECRET

"""
What I want to do:
Retrieve an author.
Write a review.
"""

url = GOODREADS = "http://www.goodreads.com"
request_token_url = '%s/oauth/request_token' % url
authorize_url = '%s/oauth/authorize/' % url
access_token_url = '%s/oauth/access_token/' % url

OAuthHook.consumer_key = GOODREADS_KEY
OAuthHook.consumer_secret = GOODREADS_SECRET

oauth_hook = OAuthHook(consumer_key=GOODREADS_KEY, consumer_secret=GOODREADS_SECRET)
print "calling hook", oauth_hook.consumer_key, oauth_hook.consumer_secret

response = requests.get(request_token_url, hooks={'pre_request': oauth_hook})
print "response", response, response.text
qs = parse_qs(response.text)
oauth_token = qs['oauth_token'][0]
oauth_secret = qs['oauth_token_secret'][0]

authorize_link = '%s?oauth_token=%s' % (authorize_url,
                                        oauth_token)
print authorize_link
accepted = 'n'
while accepted.lower() == 'n':
    # you need to access the authorize_link via a browser,
    # and proceed to manually authorize the consumer
    accepted = raw_input('Have you authorized me? (y/n) ')

def login(host, url, user):
    session = requests.Session()
    credentials = {
        "email": user['email'],
        "password": user['password']
    }

    return session.post(host+url, data=credentials)
    if res.status_code == 200:
        log.info("Logged in.")
    else:
        log.warning("Received status %d", res.status_code)

    return session

def get(ses, path, server=url):
    res = ses.get(server+path)
    print res

    return res, json.loads(res.content)

