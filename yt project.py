


import tkinter
from tkinter import *
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("750x400")
app.title("YouTube Downloader")
app.resizable(False,False)

def on_button_click():
    video_url = Entry.get()
    quality = combobox.get()

    if not video_url:
        finish_label.configure(text="Please enter a valid YouTube video URL.")
        return

    try:
        yt = YouTube(video_url)
        # Filter streams that include both video and audio
        formats = yt.streams.filter(file_extension="mp4", progressive=True, audio_codec="mp4a.40.2")
        title.configure(text=yt.title,text_color="white")
        
        if quality == 'low':
            selected_stream = formats.first()
        elif quality == 'med':
            selected_stream = formats.filter(res="720p").first()
        elif quality == 'high':
            selected_stream = formats.get_highest_resolution()
        else:
            finish_label.configure(text="Invalid quality selection.")
            return

        if selected_stream:
            selected_stream.download(f"{path.get()}")
            finish_label.configure(text="Downloaded")
        else:
            finish_label.configure(text="Selected stream is None.")
    except Exception as e:
        finish_label.configure(text=f"Error: {e}")

        
#set a background image 
img = PhotoImage(file="background.png") #give a correct path of image with its name and extension
bg_label=Label(app,image=img)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

# title of the video
title = customtkinter.CTkLabel(master=app,text="",bg_color='#2DBCC5',text_color='black')
title.place(x=40,y=180)

Entry = customtkinter.CTkEntry(master=app, placeholder_text="Give me the link...", width=300)
Entry.place(x=30, y=30)

#to give path where the video is downloaded
path = customtkinter.CTkEntry(master=app, placeholder_text="Give path here...", width=180)
path.place(x=30, y=80)

#to ask user which quality they want to download
quality_options = ['low', 'med', 'high']
combobox = customtkinter.CTkComboBox(master=app, values=quality_options)
combobox.place(x=225,y=80)

#to show the message the video is downloaded or not                                   
finish_label = customtkinter.CTkLabel(app,text="",bg_color='#2DBCC5',text_color='black')
finish_label.place(x=50,y=250)

#making a button with an image                                   
btn_img = tkinter.PhotoImage(file='button_0.png')    
button = tkinter.Button(app, image=btn_img, compound=tkinter.LEFT,background='#2DBCC5' ,command=on_button_click)
button.place(x=70,y=380)

app.mainloop()





