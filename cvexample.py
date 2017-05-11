import numpy as np
import cv2
from PIL import Image # added
#from resizeimage import resizeimage #added to resize an image
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






print("Starting...")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #the meat of how it does the detection of the face


global picChoice
global songChoice 

picChoice = '0'
songChoice = '0'



img = cv2.imread("Images/ironmanportrait.png") #this is variable to do the face detection
img2 = Image.open("Images/ironmanportrait.png") #this is the variable to do the cropping

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.3, 5)

possible = ["1","2","3","4","5","6","7"]
def question(picChoice):
    choice = raw_input("Please choose a picture between 1 - 7:  ")
    print ("You chose choice ", choice)
    #global picChoice
    picChoice = choice
    
    if not choice in possible:
        print " Sorry! Please enter a number between 1 - 7 "
        print " "
        return question(picChoice)
    return picChoice
    
def question2(songChoice):
    choice2 = raw_input("Please choose a song between 1 - 7:  ")
    songChoice = choice2
    if not choice2 in possible:
        print "Sorry! Please enter a number between 1 - 7 "
        print " "
        return question2(songChoice)
    return songChoice
    
def question3():
    correctResponse = ["yes", "y", "YES", "Yes", "YEs", "YeS","yeS","yES", "yEs"]
    choice3 = raw_input("Is it ready to send?    ")
    if not choice3 in correctResponse:
        print " Okay lets fix it..."
        print " "
        question(picChoice)
        question2(songChoice)
        question3()
    else:
        print " "
        print " Okay! sending..."
        
       
   
picChoice = question(picChoice)
print " " 
songChoice = question2(songChoice)
print " "
print " okay, let's preview your creation!"
#preview shown with audio sample hopefully
#print " "
#question3()

cv2.imwrite('Images/imagefacedetection.png', img) #creates an image to show there is a face detection
cv2.waitKey()

print("Detecting image and cropping it...")
img2.save("Images/imagecrop.png") #saves the cropped face


for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #draws a rectangle around the face
        roi_color = img[y:y+h, x:x+w]
        img2 = img2.crop((x, y, (x+w), (y+h))) #crops out the rectangle since the images are the same we can trust that there will be no issues croping from the "different" image





cv2.imwrite('Images/imagefacedetection.png', img) #creates an image to show there is a face detection
cv2.waitKey()
print("First original crop...")
print(img2)
img2.save("Images/imagecrop.png") #saves the cropped face

#the following is the relativley the same as the above code, just to give a more precise location of the face


img = cv2.imread("Images/imagecrop.png") #this is variable to do the face detection

print("Opening cropped image 2...")
img2 = Image.open("Images/imagecrop.png") #this is the variable to do the cropping

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print("Making box around face...")
for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #draws a rectangle around the face
        roi_color = img[y:y+h, x:x+w]
        img2 = img2.crop((x, y, (x+w), (y+h))) #crops out the rectangle since the images are the same we can trust that there will be no issues croping from the "different" image



print("Saving cropped image with box")
cv2.imwrite('Images/imagecropdefined.png', img) #creates an image to show there is a face detection
#cv2.waitKey()

img2.save("Images/imagecropdefinedfinal.png")


if picChoice == "1": #for the mermaid
    #the following will be to move the cropped face onto the template
    
    print("Opening background and foreground")
    #backdrop = Image.open("white-background-2.png").convert('RGBA')
    background = Image.open("Images/mermaid.png").convert('RGBA') #here we need to make the background image and forground to accept the transperency
    foreground = Image.open("Images/imagecropdefinedfinal.png").convert('RGBA')
    
    
    print("Creating face detection...")
    basewidth = 45 
    wpercent = (basewidth/float(foreground.size[0]))
    hsize = int((float(foreground.size[1])*float(wpercent))) #this black coverts the face into a smaller image
    foreground = foreground.resize((basewidth,hsize))
    foreground.save('Images/imagecropdefinedfinal.png')
    
    
    print ("Putting face on mermaid")
    background.paste(foreground, (90,55))
    background.save("Images/combinedimage.png")
    
if picChoice == "2": #for the buff guy pic
    #the following will be to move the cropped face onto the template
    
    print("Opening background and foreground")
    #backdrop = Image.open("white-background-2.png").convert('RGBA')
    background = Image.open("Images/Buff Guy.png").convert('RGBA') #here we need to make the background image and forground to accept the transperency
    foreground = Image.open("Images/imagecropdefinedfinal.png").convert('RGBA')
    
    
    print("Creating face detection...")
    basewidth = 130 
    wpercent = (basewidth/float(foreground.size[0]))
    hsize = int((float(foreground.size[1])*float(wpercent))) #this black coverts the face into a smaller image
    foreground = foreground.resize((basewidth,hsize))
    foreground.save('Images/imagecropdefinedfinal.png')
    
    
    print ("putting face on buff guy")
    background.paste(foreground, (260,10))
    background.save("Images/combinedimage.png")
    
    
if picChoice == "3": #for the nurse pic
    #the following will be to move the cropped face onto the template
    
    print("Opening background and foreground")
    #backdrop = Image.open("white-background-2.png").convert('RGBA')
    background = Image.open("Images/face_nurse.png").convert('RGBA') #here we need to make the background image and forground to accept the transperency
    foreground = Image.open("Images/imagecropdefinedfinal.png").convert('RGBA')
    
    
    print("Creating face detection...")
    basewidth = 100 
    wpercent = (basewidth/float(foreground.size[0]))
    hsize = int((float(foreground.size[1])*float(wpercent))) #this black coverts the face into a smaller image
    foreground = foreground.resize((basewidth,hsize))
    foreground.save('Images/imagecropdefinedfinal.png')
    
    
    print ("putting face on sexy nurse")
    background.paste(foreground, (150,40))
    background.save("Images/combinedimage.png")
    
    
    
if picChoice == "4": #for the baby adult pic
    #the following will be to move the cropped face onto the template
    
    print("Opening background and foreground")
    #backdrop = Image.open("white-background-2.png").convert('RGBA')
    background = Image.open("Images/FatBabyAdult.png").convert('RGBA') #here we need to make the background image and forground to accept the transperency
    foreground = Image.open("Images/imagecropdefinedfinal.png").convert('RGBA')
    
    
    print("Creating face detection...")
    basewidth = 55
    wpercent = (basewidth/float(foreground.size[0]))
    hsize = int((float(foreground.size[1])*float(wpercent))) #this black coverts the face into a smaller image
    foreground = foreground.resize((basewidth,hsize))
    foreground.save('Images/imagecropdefinedfinal.png')
    
    
    print ("putting face on the fat baby")
    background.paste(foreground, (135,30))
    background.save("Images/combinedimage.png")
    
if picChoice == "5": #for the hot tup pic
    #the following will be to move the cropped face onto the template
    
    print("Opening background and foreground")
    #backdrop = Image.open("white-background-2.png").convert('RGBA')
    background = Image.open("Images/Man Sandwich.png").convert('RGBA') #here we need to make the background image and forground to accept the transperency
    foreground = Image.open("Images/imagecropdefinedfinal.png").convert('RGBA')
    
    
    print("Creating face detection...")
    basewidth = 65
    wpercent = (basewidth/float(foreground.size[0]))
    hsize = int((float(foreground.size[1])*float(wpercent))) #this black coverts the face into a smaller image
    foreground = foreground.resize((basewidth,hsize))
    foreground.save('Images/imagecropdefinedfinal.png')
    
    
    print ("putting face on the hot tub pic")
    background.paste(foreground, (115,70))
    background.save("Images/combinedimage.png")
    
if picChoice == "6": #for the music maker pic
    #the following will be to move the cropped face onto the template
    
    print("Opening background and foreground")
    #backdrop = Image.open("white-background-2.png").convert('RGBA')
    background = Image.open("Images/MusicMaker.png").convert('RGBA') #here we need to make the background image and forground to accept the transperency
    foreground = Image.open("Images/imagecropdefinedfinal.png").convert('RGBA')
    
    
    print("Creating face detection...")
    basewidth = 65
    wpercent = (basewidth/float(foreground.size[0]))
    hsize = int((float(foreground.size[1])*float(wpercent))) #this black coverts the face into a smaller image
    foreground = foreground.resize((basewidth,hsize))
    foreground.save('Images/imagecropdefinedfinal.png')
    
    
    print ("putting face on the music maker pic")
    background.paste(foreground, (25,0))
    background.save("Images/combinedimage.png")
    
    
if picChoice == "7": #for the throne pic
    #the following will be to move the cropped face onto the template
    
    print("Opening background and foreground")
    #backdrop = Image.open("white-background-2.png").convert('RGBA')
    background = Image.open("Images/OnTheThrone.png").convert('RGBA') #here we need to make the background image and forground to accept the transperency
    foreground = Image.open("Images/imagecropdefinedfinal.png").convert('RGBA')
    
    
    print("Creating face detection...")
    basewidth = 80
    wpercent = (basewidth/float(foreground.size[0]))
    hsize = int((float(foreground.size[1])*float(wpercent))) #this black coverts the face into a smaller image
    foreground = foreground.resize((basewidth,hsize))
    foreground.save('Images/imagecropdefinedfinal.png')
    
    
    '''
    img3 = cv2.imread('Images/imagecropdefinedfinal.png',0) #this block is doing the rotation
    rows,cols = img3.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    img3.save('Images/imagecropdefinedfinal.png')
    '''
    
    #forground = foreground.rotate(45)
    
    #foreground.save('Images/imagecropdefinedfinal.png')
    
    
    print ("putting face on the toilet pic")
    background.paste(foreground, (130,40))
    background.save("Images/combinedimage.png")

print("Finished... open combinedimage.png")



print " "
question3()




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

print("please enter the image you want to send. Include folder (ex: Images/nameofpicture.png")

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

'''
for (x,y,w,h) in faces:
        cv2.ellpise(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #draws a rectangle around the face
        roi_color = img[y:y+h, x:x+w]
        img2 = img2.crop((x, y, (x+w), (y+h))) #crops out the rectangle since the images are the same we can trust that there will be no issues croping from the "different" image



backdrop = backdrop.resize((290,200))
backdrop.save("white-background-2.png")

pixdata = background.load()

width, height = background.size
for y in xrange(height):
    for x in xrange(width):
        if pixdata[x, y] >= (250, 250, 250, 250): #thank you stack overflow converts white space to tansparent on the mermaid face
            pixdata[x, y] = (255, 255, 255, 0)
background.save("mermaid.png")



foreground.paste(background, (90,55))
foreground.save("combinedimage.png")

background.paste(foreground, (90,55))
background.save("combinedimage.png")

backdrop.paste(foreground, (90,55))
backdrop.save("combinedimage.png")


backdrop.paste(background, (0,0))
backdrop.save("combinedimage.png")

foreground.size = (15,15)
background.size = (100, 100) #need to work on resizing image


background.size = foreground.size
Image.alpha_composite(background, foreground).save("combinedimage.jpg")


background.paste(foreground, (0, 0), foreground)
background.show()
background.save("combinedimage.jpg")
'''