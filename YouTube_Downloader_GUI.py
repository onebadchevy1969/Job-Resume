import tkinter, os, customtkinter
from tkinter import *

from pytube import YouTube
from tkinter import filedialog


link = ""
curr_dir = ""

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x400")



def YT_Link(event=None):
    link = str(entry_1.get())
    YT = YouTube(link)
    ytv = YT.streams.get_highest_resolution()
    ytv.download(r'{}'.format(curr_dir)) # you cannot download a video in just the drive letter (ex: E:\) it has to be in a folder to, try to resolve the issue later down the line
    label_download_done = customtkinter.CTkLabel(master=frame, text="Download is Done!") #This is to show that the Download is done
    label_download_done.pack(pady=24, padx=20)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="YouTube Video Downloader", font=("Roboto", 20))
label.pack(pady=12, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame, placeholder_text="YouTube Video Link")
entry_1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Download Video", command=YT_Link)
button.pack(pady=12, padx=10)

#this is to ask if the user would like the download to go into a different dir then before
def Ask_dir():
    global curr_dir
    curr_dir = tkinter.filedialog.askdirectory()
    label_dir = customtkinter.CTkLabel(master=frame, text="current dir: {}".format(curr_dir))
    label_dir.pack(pady=12, padx=10)

browse_button = customtkinter.CTkButton(master=frame, text="Change File Destination", command=Ask_dir) #this button is to change the dir of where the download is going to take place
browse_button.pack(pady=12, padx=10)

root.bind('<Return>', YT_Link)  # this line is so that you can press 'enter' and have the YT_link() function play out

root.mainloop()
