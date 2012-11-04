import requests
import local

URI = "http://www.goodreads.com/author/show"
GOODREADS_KEY = local.GOODREADS_KEY
ALICE_MUNRO_ID = 6410

params = {
    "key": GOODREADS_KEY,
    "id":  ALICE_MUNRO_ID,
    }

response = requests.get(URI, params=params)
print response
print response.content
