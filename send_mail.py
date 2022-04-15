#/data/xce/local//python/bin/python2.7
# -*- coding:utf-8 -*-

import smtplib
import base64
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import COMMASPACE
import sys

SENDER = ''
SMTP_SERVER = 'smtp.gmail.com'
USER_ACCOUNT = {'username':str(sys.argv[1]), 'password':str(sys.argv[2])}
SUBJECT = "Test Test"


def send_mail(receivers, text, sender=SENDER, user_account=USER_ACCOUNT, subject=SUBJECT):
    msg_root = MIMEMultipart()  
    msg_root['Subject'] = subject  
    msg_root['To'] = COMMASPACE.join(receivers)  
    msg_text = MIMEText(text, 'html', 'utf-8')  
    msg_root.attach(msg_text)  

    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user_account['username'], user_account['password'])
    smtp.sendmail(sender, receivers, msg_root.as_string())

if __name__=="__main__":
    send_mail([str(sys.argv[3])],"pig")
