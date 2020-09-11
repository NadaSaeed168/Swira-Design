import datetime
import requests
import json,urllib.request
from collections import Counter

# get the date that is 30 days from now
start_date = datetime.date.today() + datetime.timedelta(-30)
print(start_date)

# put the date in the url to call api and load data from json
url = 'https://api.github.com/search/repositories?q=created:>' + str(start_date) + '&sort=stars&order=desc&page=1'
data = urllib.request.urlopen(url).read()
output = json.loads(data)
print (url)

# get the unique languages from the json file data
ul = []
for item in range(len(output['items'])):
    if output['items'][item]['language'] not in ul:
        ul.append(output['items'][item]['language'])

# loop on the unique languages array and 
# print the name of the repositories used this language and the count of the repos that used this language
for x in ul:
    count = 0
    print(x)
    for item in range(len(output['items'])):
        if x == output['items'][item]['language']:
            print(output['items'][item]['name'], sep='\n')
            count = count + 1
    print(count)
    count = 0