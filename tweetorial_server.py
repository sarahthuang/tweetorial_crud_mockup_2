from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask_cors import CORS
import get_tweet

app = Flask(__name__)
CORS(app)

import datetime
import json

leads = []
filtered = []
annotations = []

i = "./starter_tweets.txt"
in_file = open(i, "r")
leads = json.loads(in_file.read())

def searchforword(arr, searchWord):
    searchWord = searchWord.lower()
    for key in arr:
        if searchWord in key["Title"].lower() or searchWord in key["Text"].lower() or searchWord in key["Author"].lower() or searchWord in key["LeadTypes"][0] or searchWord in key["LeadTypes"]:
            filtered.append(key)

    return filtered

@app.route('/')
def search():
    savetweets()
    return render_template('./searchpage.html', leads=leads)

@app.route('/getthismany', methods=['GET', 'POST'])
def gethismany():
    filtered.clear()
    num = request.get_json()
    num = num + 1
    # last element #
    last = int(len(leads))
    first = int(len(leads))-(num-1)

    for x in range(first, last):
        filtered.insert(0, leads[x])

    return jsonify(filtered=filtered)

@app.route('/searchbykeyword', methods=['GET', 'POST'])
def searchbykeyword():
    filtered.clear()
    searchword = request.get_json()
    searchforword(leads, searchword)
    return jsonify(filtered=filtered)

@app.route('/view/<id>', methods=['GET', 'POST'])
def view(id):
    tweet = leads[int(id)]
    return render_template('templatepage.html', tweet=tweet)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_prefill')
def create_prefill():
    return render_template('create_prefill.html')

@app.route('/createtweet_prefill', methods=['GET', 'POST'])
def createtweet_prefill():
    newtweet = request.get_json()
    length = len(leads)
    newtweet["Id"] = length
    tweet_called=get_tweet.get_dict(newtweet["Link"])
    print(tweet_called)
    newtweet["Author"]=tweet_called["user"]["name"]
    newtweet["Date"]=tweet_called["created_at"]
    newtweet["Text"]=tweet_called["text"]
    leads.append(newtweet)
    link = "view/" + str(length)
    savetweets()
    return jsonify(link=link)

@app.route('/createtweet', methods=['GET', 'POST'])
def createtweet():
    newtweet = request.get_json()
    length = len(leads)
    newtweet["Id"] = length
    leads.append(newtweet)
    link = "view/" + str(length)
    savetweets()
    return jsonify(link=link)

#@app.route('/edit/<id>', methods=['GET', 'POST'])
#def edit(id):
    #title = leads[int(id)]["Title"]
    #print("392")
    #return render_template('editpage.html', id=id)

@app.route('/edit_Title', methods=['GET','POST'])
def edit_Title():
    data = request.get_json()
    title = data[0]
    index = data[1]
    leads[int(index)]["Title"] = title
    #print(leads[int(index)])
    savetweets()
    return jsonify('')

@app.route('/edit_Author', methods=['GET','POST'])
def edit_Lead():
    data = request.get_json()
    author = data[0]
    index = data[1]
    leads[int(index)]["Author"] = author
    #print(leads[int(index)])
    savetweets()
    return jsonify('')

#@app.route('/deleteitem', methods=['GET', 'POST'])
#def deleteitem():
#    id = request.get_json()
#    leads.remove(leads[int(id)])
#    if len(leads) != 0:
#        for x in range(0, len(leads)):
#            leads[x]["Id"] = x
#    else:
#        print("there are no more entries left! please add some")
#    return jsonify(leads=leads)

@app.route('/deleteleadtype', methods=['GET', 'POST'])
def deleteleadtype():
    content = request.get_json()
    index = content[0]
    id = content[1]
    leads[id]["LeadTypes"][int(index)]["marked_as_deleted"] = True
    return jsonify('')

@app.route('/undodeleteleadtype', methods=['GET', 'POST'])
def undodeleteleadtype():
    content = request.get_json()
    index = content[0]
    id = content[1]
    leads[id]["LeadTypes"][int(index)]["marked_as_deleted"] = False
    typetoreturn = leads[id]["LeadTypes"][int(index)]["Type"]
    return jsonify(typetoreturn = typetoreturn)

@app.route('/getnondeleted', methods=['GET', 'POST'])
def getnondeleted():
    index = request.get_json()
    result = leads[index]["LeadTypes"]
    return jsonify(result=result)

@app.route('/annotate', methods=['GET', 'POST'])
def annotate():
    return render_template('annotate.html')

def savetweets():
    ts = datetime.datetime.now().timestamp()
    o = "./backup/" + repr(ts) + ".txt"
    out_file = open(o, "w")
    out_file.write(json.dumps(leads))
    out_file.close()

@app.route('/accessfromTwitter')
def accessfromTwitter():
    return render_template('access.html')


#gittesting
if __name__ == '__main__':
   app.run(debug = True)
