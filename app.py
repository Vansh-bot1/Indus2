from flask import Flask,jsonify
import smtplib
from email.message import EmailMessage
app=Flask(__name__)
@app.route('/')
def hello():
	return 'TMKC'

@app.route('/fun/<string:name>/<string:email>')	
def fun(name,email):
	msg=EmailMessage()
	msg['Subject']='Just Checking'
	msg['From']='v.r.goel2004@gmail.com'
	msg['To']=email
	msg.set_content('My API is ready for Hosting '+name)
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login('v.r.goel2004@gmail.com','qfutofqohvbddyxe')
		smtp.send_message(msg)
	return 'Check your Inbox'

if __name__=='__main__':
	app.run(debug=True)