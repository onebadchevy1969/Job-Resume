import qrcode, os
from pathlib import Path
print('QRcode generator ')
qr_code = input('What would you like to encode?') #This asks what text or website page you would like to make into a QRcode
img = qrcode.make(qr_code) #This takes the website/text that was entered by the user from the last line, and makes it into a QRcode
Name = input("What would you like to call the file?")#asks what you want to name the file
img.save(Name + '.jpg')#creates the QRcode file with the name that was enterned with the file extention '.jpg' in order for the QRcode to be opended
print('Ok, saved as ' + Name + '.jpg')
print('It is saved in ' + Path.cwd()) #shows where the QRcode was saved
