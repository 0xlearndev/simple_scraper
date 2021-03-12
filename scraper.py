''' A simple webpage scraper
    Usage: python3 scraper.py URL
    Returns: 
 '''

import requests
import time
import sys
import uuid

args_in = sys.argv # list of arguments
if len(args_in) == 1: # if only 1 argument then user forgot to specify URL
    print("You missed the URL argument")
    sys.exit()

if len(args_in) > 2: # if more than 2 arguments, user messed up somewhere
    print("Too many arguments.")
    sys.exit()


class URLObject:
    def __init__(self, URL):
        self.link = str(URL)
        self.friendly_link = self.link.split('//')[1]  # Split from https:// so we get the domain name
        self.unique_id = str(uuid.uuid4())[:6]  # get a short unique id
    def friendlylink(self):
        print("Friendly link: {}".format(self.friendly_link))

    def printheaders(self):
        print("Getting info for {}".format(self.link))
        r = requests.get(self.link)
        for k,v in r.headers.items():
            print("Key: {}\nValue(s): {}\n".format(k,v))

    def saveheaders(self):
        print("Getting info for {}".format(self.link))
        r = requests.get(self.link)
        print('Saving response dict.')
        with open('{}-{}-headers.txt'.format(self.friendly_link, self.unique_id), 'w') as f:
            for k,v in r.headers.items():
                f.write('{}: {}\n'.format(k,v))





URL = str(args_in[1]) # get URL from terminal
newurl = URLObject(URL) # create URLObject obj passing the URL from terminal
newurl.friendlylink() # show friendly link
newurl.printheaders()
newurl.saveheaders()

