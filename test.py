import smtplib
import getpass

#///////
#import mimetypes
#from email.mime.image import MIMEImage
#////////
#fileToSend = "volcano.jpg"
#img = ("volcano.jpg")
#####
#find a function to add the @

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

#myemail = input("abiblarz@csumb.edu")

#recip = input("abiblarz@csumb.edu")
recip = raw_input("Please enter the email you want to send. ")
print("email " + recip)
#need to find the attachment for the image

#/volcano.jpg

server.login(myemail, mypwd)

msg = ('git hub site: https://github.com/diegocsumb42/project3')
msg = raw_input("Enter your message:  ")
'''
####
ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
    

fp = open('volcano.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
'''
#######


#print msg.as_string()

#print(img)

print("message " + msg)


# naelshiab.com/tutorial-send-email-python/


server.sendmail(myemail, recip, msg)
server.quit()