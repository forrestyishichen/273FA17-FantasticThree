#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
import datetime

# Flask app should start in global layout
app = Flask(__name__)

book_record = {}
detail = []

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    branch_price = {'San Francisco':60.00, 'San Mateo':50.00, 'Palo Alto':100.00, 'Cupertino':80.00, 'San Jose':0.00}
    room_price = {'single':150.00, 'queen':200.00, 'king':200.00, 'twin':200.00, 'double-double':300.00, 'studio':500.00}
    if req.get("result").get("action") == "check.price":
        result = req.get("result")
        parameters = result.get("parameters")
        branch = parameters.get("branch")
        bed = parameters.get("bed")

        speech = "The cost of a " + bed + " room in " + branch + " is " + str(int(branch_price[branch])+int(room_price[bed])) + " dollars."

        print("Response:")
        print(speech)

        return {
            "speech": speech,
            "displayText": speech,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-onlinestore-shipping"
            }
    elif req.get("result").get("action") == "book.room":
        result = req.get("result")
        parameters = result.get("parameters")
        branch = parameters.get("branch")
        bed = parameters.get("bed")
        check_in_date = parameters.get("check_in_date")
        check_out_date = parameters.get("check_out_date")
        phone = parameters.get("phone")

        entry = [bed, branch, check_in_date, check_out_date, phone]
        num = len(detail)
        detail.append(entry)
        book_record[phone] = num

        speech = "Great, I will book a " + bed + " room in " + branch + " from " + check_in_date + " to " + check_out_date + " for you. Your phone is " + phone + ". Your cost will be " + str(int(branch_price[branch])+int(room_price[bed])) + " dollars per day."

        print("Response:")
        print(speech)

        return {
            "speech": speech,
            "displayText": speech,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-onlinestore-shipping"
            }
    elif req.get("result").get("action") == "check.book":
        result = req.get("result")
        parameters = result.get("parameters")
        phone = parameters.get("phone")
        
        key =book_record[phone]
        print(key)
        print(detail[key])

        speech = "Great, You have booked a " + detail[key][0] + " room in " + detail[key][1] + " from " + detail[key][2] + " to " + detail[key][3] + "."

        print("Response:")
        print(speech)

        return {
            "speech": speech,
            "displayText": speech,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-onlinestore-shipping"
            }    
    else:
        return {}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(port)

    print ("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
