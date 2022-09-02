import smtplib
from email.mime.text import MIMEText

class SendEmail:

    def __init__(self, email_sender, password, email_recipient):
        self.email_sender = email_sender
        self.password = password
        self.email_recipient = email_recipient

    def send_message(self, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(self.email_sender, self.password)
            msg = MIMEText(message)
            msg["subject"] = 'Topic'
            server.sendmail(self.email_sender, self.email_recipient, msg.as_string())
            return "The message was sent succesfully"
        except Exception as _ex:
            return f"{_ex}\nCheck your login or password"


sender = input("Enter the sender email: ")
password = input("Enter the sender password, if use gmail then enter application password: ")
recipient = input("Enter the recipien email: ")

msg = input("Enter any text you want to send: ")

a = SendEmail(sender, password, recipient)
print(a.send_message(msg))
