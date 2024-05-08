from tkinter import *
from time import *
# from PIL import ImageTk, Image

def time_now():
    local_time = strftime("%I:%M:%S %p")
    label_time.config(text=local_time)
    label_time.after(1000,time_now)

window = Tk()
window.title("Clock")

# icon = ImageTk.PhotoImage(Image.open("clock.png"))
# window.iconphoto(True,icon)

label_time = Label(window,font=("Arial",100),bg="black",fg="#00FF00")
label_time.pack(pady=5)
label_day = Label(window,text=strftime("%A, %B %d %Y"),font=("Arial",50),fg="black")
label_day.pack(pady=5)

time_now()


window.mainloop()