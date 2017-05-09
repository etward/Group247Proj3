import smtplib
import getpass
import os

from email.mime.multipart import MIMEMultipart
import mimetypes
from email import encoders


from argparse import ArgumentParser


from email.mime.image import MIMEImage


from email.mime.base import MIMEBase

fp = open('volcano.jpg', "rb")
#msgImage = MIMEImage(fp.read())


print(fp)
#print(msgImage)