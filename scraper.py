''' A simple webpage scraper
    Usage: python3 scraper.py URL
    Returns: 
 '''

import requests
import time
import sys
import uuid
import pathlib

args_in = sys.argv # list of arguments
if len(args_in) == 1: # if only 1 argument then user forgot to specify URL
    print("You missed the URL argument. Defaulting to https://learndev.me")
    default = True

if len(args_in) > 2: # if more than 2 arguments, user messed up somewhere
    print("Too many arguments.")
    sys.exit()

logs_path = 'saved_logs/'
pathlib.Path(logs_path).mkdir(parents=True, exist_ok=True) # create folder for saved files

class URLObject:
    def __init__(self, URL):
        self.link = str(URL)
        self.friendly_link = self.link.split('//')[1]  # Split from https:// so we get the domain name
        self.unique_id = str(uuid.uuid4())[:6]  # get a short unique id

    def get_text(self):
        r = requests.get(self.link)
        return str(r.text)
    
    def save_text(self):
        print("Getting text for {}".format(self.link))
        r = requests.get(self.link)
        with open('{}{}-{}-text.txt'.format(logs_path, self.friendly_link, self.unique_id), 'w') as f:
            f.write(r.text)
        print('Saved text')

    def friendlylink(self):
        print("Friendly link: {}".format(self.friendly_link))
        return str(self.friendly_link)

    def printheaders(self):
        print("Getting info for {}".format(self.link))
        r = requests.get(self.link)
        for k,v in r.headers.items():
            print("Key: {}\nValue(s): {}\n".format(k,v))

    def saveheaders(self):
        print("Getting info for {}".format(self.link))
        r = requests.get(self.link)
        print('Saving response dict.')
        with open('{}{}-{}-headers.txt'.format(logs_path, self.friendly_link, self.unique_id), 'w') as f:
            for k,v in r.headers.items():
                f.write('{}: {}\n'.format(k,v))

if default: # if no URL is specified, default to this
    URL = "https://learndev.me"
if not default:
    URL = str(args_in[1]) # get URL from terminal

newurl = URLObject(URL) # create URLObject obj passing the URL from terminal
newurl.friendlylink() # show friendly link
newurl.printheaders()
newurl.saveheaders()
print(newurl.get_text())
newurl.save_text()