#!/usr/bin/python
import time
import sys  
import smtplib  
sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
                                                
from bridgeclient import BridgeClient as bridgeclient
                                                     
TO = 'your email address here'
GMAIL_USER = 'your gmail account here'
GMAIL_PASS = 'your gmail password here'
SUBJECT = 'Digital pin changed value!!'
TEXT = 'Your digital pin went HIGH'
value = bridgeclient()                              
                                                     
#function to send email 
def send_email(sensorValue):
 	print("Sending Email")
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(GMAIL_USER, GMAIL_PASS)
	header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
	header = header + '\n' + 'Subject:' + SUBJECT + '\n'
	print header
	msg = header + '\n' + TEXT + ' \n\n' + TEXT2 + ' \n\n'
	smtpserver.sendmail(GMAIL_USER, TO, msg)
	smtpserver.close()

value = bridgeclient()

while True:
	message = value.get("D7")
	print message
 	if message == '1' :
 		#send_email()
		print "sending email, D7 went high!"
		TEXT2 =  "A0 analog value: "+ value.get("A0")
		print TEXT2
	elif message == "0":
		print "D7 low"
	else:
		print "no message"
	
	time.sleep(2)
