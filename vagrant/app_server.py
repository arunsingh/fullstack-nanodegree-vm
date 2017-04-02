# THIS IS A WEBSERVER FOR DEMONSTRATING THE TYPES OF RESPONSES WE SEE FROM
# AN API ENDPOINT

from flask import Flask


app = Flask(__name__)


# GET Request

@app.route('/readHello')
def getRequestHello():
    return "Hi, I got your Request!!"


# Post Request
@app.route('/createHello', methods=['POST'])
def postRequestHello():
    return "I see you a sent POST message :)"


# Update Request
@app.route('/updateHello', methods=['PUT'])
def updateRequestHello():
    return "Sending Hello on Put Request!"


# Delete Request
@app.route('/deleteRequest', methods=['DELETE'])
def deleteRequestHello():
    return "Hey, I am wiping out your Hard Disk, Enjoy...Hahaha, Just Kidding, Request deleted$"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
