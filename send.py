import smtplib 
import email
from email.message import EmailMessage
from user_info import MY_EMAIL, PASSWORD_KEY, MESSAGE

# SMTP Server and port no for GMAIL.com
gmail_server= "mail.inbox.lv"
gmail_port= 587


# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
    
# Login with your email and password
my_server.login(MY_EMAIL, PASSWORD_KEY)
msg = EmailMessage()
msg.set_content(MESSAGE)

msg['Subject'] = 'Testa mail'
msg['From'] = MY_EMAIL
msg['To'] = MY_EMAIL
msg['CC'] = MY_EMAIL

my_server.send_message(msg)
print('Mail Sent to', msg['To'], msg['CC'])
# print(msg)