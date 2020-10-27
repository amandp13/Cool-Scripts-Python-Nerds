import smtplib


def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    email = 'Enter Email Here'
    password = 'Enter Password Here'

    server.login(email,password)

    sender = email
    reciever = email
    msge = 'Enter Message Here'

    server.sendmail(sender,reciever,msge)