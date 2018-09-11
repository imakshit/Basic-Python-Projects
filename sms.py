import requests

username = "" #from twilio account
account_sid = username
password = "" #from twilio account

number_to_text = "" #enter the number to send the message to
twilio_number = "" # enter the twilio verified number

message_body = "Hi , congrats on recieving the msg"

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)

base_url = "https://api.twilio.com/2010-04-01/Accounts"
message_url = base_url+"/"+ account_sid + "/Messages"
auth_cred = (username , password)

post_data = {
"From" : twilio_number,
"To": number_to_text,
"Body": message_body,
    }

r = requests.post(message_url , data = post_data , auth = auth_cred)

print(r.status_code)
xml_pretty(r.text)
