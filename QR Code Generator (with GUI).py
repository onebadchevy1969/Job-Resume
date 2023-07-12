import tkinter, os, customtkinter, qrcode
from tkinter import filedialog
from pathlib import Path
from PIL import ImageTk, Image
from tkinter import *

    #setting any needed variables
curr_dir = ''
QR_file_name = ''
path = ''
img = ''

    #settting what the GUI will look like
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x600")

frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

def Make_QR_Code(event=None):
    global QR_file_name, path, img #having all of these variables change globally and not just in this function

    qr_code_link = str(QR_Link_Entry.get()) #calls for the link/text that is going to be made into a QR Code
    QR_file_name = str(File_name_Entry.get()) #calls for the file name that was passed though in the File_name_Entry
    path = r'{}/{}.jpg'.format(curr_dir,QR_file_name)
    img = qrcode.make(qr_code_link) #make a QR Code
    img.save(path) #save the file as a .jpg, so it can be viewed as an image
    Display_QR_CODE()

def Display_QR_CODE():
    open_QR_code = ImageTk.PhotoImage(file=str(path)) #sets the path of the image to be a photo image with tkinter
    LABEL_open_QR_code = Label(root, image=open_QR_code)
    LABEL_open_QR_code.photo = open_QR_code #this sets the image as an anchor, if this is not here, it will just display a blank image
    LABEL_open_QR_code.pack() #creates the label that will display the image

def Ask_dir():
    global curr_dir

    curr_dir = tkinter.filedialog.askdirectory()
    label_dir = customtkinter.CTkLabel(master=frame, text="current directory: {}".format(curr_dir))
    label_dir.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="QR Code Generator", font=("Roboto", 20))
label.pack(pady=12, padx=10)

QR_Link_Entry = customtkinter.CTkEntry(master=frame, placeholder_text='QR Code Link')
QR_Link_Entry.pack(pady=12, padx=10)

File_name_Entry = customtkinter.CTkEntry(master=frame, placeholder_text='Name For The File')
File_name_Entry.pack(pady=12, padx=10)

# this is to ask if the user would like the download to go into a different dir then before
browse_button = customtkinter.CTkButton(master=frame, text="Change File Destination", command=Ask_dir) #this button is to change the dir of where the download is going to take place
browse_button.pack(pady=12, padx=10)

Gen_QR = customtkinter.CTkButton(master=frame, text='Generate QR Code', command=Make_QR_Code)
Gen_QR.pack(pady=12, padx=10)

root.bind('<Return>', Make_QR_Code)  # this line is so that you can press 'enter' and have the Make_QR_CODE() function play out

root.mainloop()
