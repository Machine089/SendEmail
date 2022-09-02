import os
import smtplib
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SendEmail:

    def __init__(self, email_sender, password, email_recipient):
        self.email_sender = email_sender
        self.password = password
        self.email_recipient = email_recipient

    def send_message(self, message, attach=None):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(self.email_sender, self.password)
            msg = MIMEMultipart()
            msg["subject"] = 'Topic'

            if message:
                msg.attach(MIMEText(message))

            if attach:
                for file in os.listdir("attachments"):
                    filename = os.path.basename(file)
                    ftype, encoding = mimetypes.guess_type(file)
                    file_type, subtype = ftype.split("/")
            
                    if file_type == 'text':
                        with open(f"attachments/{file}") as f:
                            file = MIMEText(f.read())
                    elif file_type == 'image':
                        with open(f"attachments/{file}", "rb") as f:
                            file = MIMEImage(f.read(), subtype)
                    elif file_type == 'audio':
                        with open(f"attachments/{file}", "rb") as f:
                            file = MIMEAudio(f.read(), subtype)
                    elif file_type == 'application':
                        with open(f"attachments/{file}", "rb") as f:
                            file = MIMEApplication(f.read(), subtype)
                    else:
                        with open(f"attachments/{file}", "rb") as f:
                            file = MIMEBase(file_type, subtype)
                            file.set_payload(f.read())
                            encoders.encode_base64(file)

                    file.add_header('content-disposition', 'attachment', filename=filename)
                    msg.attach(file)


            server.sendmail(self.email_sender, self.email_recipient, msg.as_string())
            return "The message was sent succesfully"
        except Exception as _ex:
            return f"{_ex}\nCheck your login or password"


sender = input("Enter the sender email: ")
password = input("Enter the sender password, if use gmail then enter application password: ")
recipient = input("Enter the recipien email: ")

msg = input("Enter any text you want to send: ")
attach = input("Attach files from a directory? ")

a = SendEmail(sender, password, recipient)
a.send_message(msg, attach)
