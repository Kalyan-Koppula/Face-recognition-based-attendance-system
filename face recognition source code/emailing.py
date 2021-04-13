# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:19:22 2021

@author: kalya
"""

import smtplib, ssl,datetime

sender= "sender@gmail.com"     #senders email id
password="pwd"                #password



def email_pin(email,pin):
    port = 465
    now=datetime.datetime.now()
    date=now.strftime('%m/%d/%Y').replace('/0','/')
    if(date[0]=='0'):
        date=date[1:]
    subject="Pin for your attendance app "
    text="\nYour pin for attendance app is "+str(pin)

    message ='Subject: {}\n\n{}'.format(subject, text)
    

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, email, message)

    print("sent email!")



def send_email(receiver_mail,attendance):
    port = 465
    now=datetime.datetime.now()
    date=now.strftime('%m/%d/%Y').replace('/0','/')
    subject="Attendance on "+str(date)
    text="\nYour attendance is marked "+attendance

    message ='Subject: {}\n\n{}'.format(subject, text)
    

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver_mail , message)

    print("sent email!")