from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dialogflow import reply

app = Flask(__name__)

@app.route("/")

def generic():
    return "Hello! there"

@app.route("/sms",methods=['POST'])

def respond():

    msg = request.form.get('Body')
    phone_no = request.form.get('From')

    reply= reply(msg,phone_no)
    resp.message(reply)

    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)


if __name__=="__main__":
    app.run(debug=True)