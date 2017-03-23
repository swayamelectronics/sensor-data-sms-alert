from flask import (json)
import time
import requests
from twilio.rest import TwilioRestClient

def send_sms(temp):
    """Sends sms via Twilio"""
    sid='Your twilio sid'
    token='Your Twilio token'
    body= "Temperature is cross threshold .Current Temperature is %s " % temp
    to= '+919176726702'
    from_number= '+15132782151'
    ACCOUNT_SID = sid
    AUTH_TOKEN = token
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        to=to,
        from_=from_number,
        )
    print message.sid
    res = str(message.sid)
    return res
    print(data['value'])

while True:
        time.sleep(5)
        response = requests.get('http://cloud.boltiot.com/remote/e6911e6a-7ed4-42ab-82d0-2dde8ca15b6c/analogRead?pin=A0&deviceName=BOLT360470')
        data = json.loads(response.text)
        var = int(data['value'])
	if var > 500:
                print  "temperature is=", (data['value'])
                print "sending sms"
                send_sms(var) 
        else:
                print  "temperature is=", (data['value'])
                print "temperature is normal"
		
