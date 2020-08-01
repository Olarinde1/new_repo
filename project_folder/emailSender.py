import smtplib
to = input('Enter the email of reciepient:\n')
content = input('Enter the content of mail::\n ')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # make communication between the smtplib server and email
    server.starttls() # starts the session
    server.login('olarindeallioluwanifemi@gmail.com')
    server.sendmail('olarindeallioluwanifemi@gmail.com', to, content)
    server.close()
    print('mail sent successfully')
sendEmail(to, content)

