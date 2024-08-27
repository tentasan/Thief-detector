from twilio.rest import Client

account_sid='ACa29bb463cda5b3c8070ef99bd410e66b'
auth_token='09d9284197f622fb868cbb66a8b5f9bb'

Client=Client(account_sid,auth_token)

to_number='+917010850916'
from_number='+12513135335'

call=Client.calls.create(
    twiml='<Response><Say>burglar detected</Say></Response>',
    to=to_number,
    from_=from_number
)
print(call.sid)