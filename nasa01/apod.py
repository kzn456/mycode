#!/usr/bin/python3

import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=zPKZMIPCdqWTz4mwSu2SWS5rFsAMIsbtI4tEe2da'

apodurlobj = urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))

print("\n\nConverted python data")
print(decodeapod)

input('\nPress Enter to open NASA Picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])

