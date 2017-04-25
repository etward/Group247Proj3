import smtplib
import getpass

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
#/volcano.jpg

server.login(myemail, mypwd)

msg = raw_input("Enter your message:  ")

print("message " + msg)

msg.attach()



server.sendmail(myemail, recip, msg)
server.quit()