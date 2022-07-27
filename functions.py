from app import session


import smtplib
from email.message import EmailMessage
from click import password_option
from matplotlib import use

def checkiflogged():
    if "username" in session:
        return True
    if "name" in session:
        return True

    else:
         return False

def email_alert(subject , body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = "acadimicadvising@gmail.com"
    msg['from'] = user
    password = "rhlysldzvxhqitqi"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()    
if __name__ == "__main__":
    email_alert("Sessions request","There is a new session request","moustafasamy490@gmail.com")


def check_if_isadmin():
    if (session["ismadmin"] == True):
        return True
    else:
        return False
