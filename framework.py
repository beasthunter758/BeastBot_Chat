from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")

def generic():
    return "Hello! there"

@app.route("/sms",methods=['POST'])

def respond():

    msg = request.form.get('Body')

    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)


if __name__=="__main__":
    app.run(debug=True)