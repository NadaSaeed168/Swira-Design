import flask
import datetime
import requests
import json,urllib.request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    # get the date that is 30 days from now
    start_date = datetime.date.today() + datetime.timedelta(-30)

    # put the date in the url to call api and load data from json
    url = 'https://api.github.com/search/repositories?q=created:>' + str(start_date) + '&sort=stars&order=desc&page=1'
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)

    # get the unique languages from the json file data
    ul = []
    total = []
    for item in range(len(output['items'])):
        if output['items'][item]['language'] not in ul:
            ul.append(output['items'][item]['language'])

    # loop on the unique languages array and 
    # print the name of the repositories used this language and the count of the repos that used this language
    for x in ul:
        count = 0
        # list has language, its repositories names and count of repositories
        language = []
        language.append(x)
        for item in range(len(output['items'])):
            if x == output['items'][item]['language']:
                language.append(output['items'][item]['name'])
                count = count + 1
        language.append(count)
        total.append(language)
        count = 0
    # returns a arraylist of arraylists that each list contains the repos that used it and their count number
    return json.dumps(total)
    
app.run()