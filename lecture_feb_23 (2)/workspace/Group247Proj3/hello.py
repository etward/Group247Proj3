import smtplib
import getpass
import os

from email.mime.multipart import MIMEMultipart
import mimetypes

from email.mime.text import MIMEText
from email import encoders


from argparse import ArgumentParser


from email.mime.image import MIMEImage


from email.mime.base import MIMEBase






try:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
except:
  print("Something went wrong")

# make connection secure
server.starttls()


myemail = raw_input("What's your email? ")
print("Email " + myemail)

mypwd = getpass.getpass('Enter your password: ')  


recip = raw_input("Please enter the email you want to send. ")
print("email " + recip)


server.login(myemail, mypwd)


message = raw_input("Enter your message:  ")

subject = raw_input("Enter the subject: ")

print("please enter the image you want to send.")

choose = raw_input("      ")

msg = MIMEMultipart()
ImageFile = open(choose, 'rb').read()
image = MIMEImage(ImageFile, name = os.path.basename(choose)) 
msg.attach(image)
msg['Subject'] = subject
text = MIMEText(message)
msg.attach(text)





server.sendmail(myemail, recip, msg.as_string())
server.quit()