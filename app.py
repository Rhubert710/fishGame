from flask import Flask
from flask import render_template

from flask import request
import json




app = Flask(__name__)

@app.route("/")
def hello_world():

    json_data =''
    with open('static/highScores.txt') as f:
        for l in f:
            json_data+=l
    
    # print(json_data)
    # print(type(json_data))
    return render_template('index.html', highScoresJSON=json.dumps(json_data))


@app.route("/postHighScores", methods=['POST'])
def postHighScores():

    # print(type(request.json))
    # print(request.json)
    # try:
    jStr = json.dumps(request.json)
    # print(type(jStr))
    # print(jStr)
    f = open("static/highScores.txt", "w")
    f.write(jStr)
    f.close()
    return "ok"
    # except:
    #     return "ERROR HOMIE: Your score did not post!"