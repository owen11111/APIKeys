import urllib.request

test = urllib.request.Request('http://127.0.0.1:5000/API/forms', headers={'APIkey': '1234'})

urllib.request.urlopen(test)