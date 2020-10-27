import smtplib


def send_email(email, password, msg):
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()
    server.login(email,password)

    sender = email
    reciever = email
    server.sendmail(sender,reciever,msg)