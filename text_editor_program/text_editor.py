import os.path
from tkinter import *
from tkinter import filedialog,colorchooser,font,messagebox
from PIL import ImageTk,Image
import os

option_size = [size for size in range(1,101)] # lựa chọn cỡ chữ

def color_change():
    color = colorchooser.askcolor() # ((R,G,B),"hex color")
    text_area.config(fg=str(color[1]))

def font_change(*args):
    text_area.config(font=(font_name.get(),font_size.get()))

def new_file():
    if len(text_area.get(1.0,"end-1c")) > 0:
        save_file()
    window.title("Untitled")
    text_area.delete(1.0,"end-1c")

def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Acer\\PycharmProjects\\HelloWorld\\game_and_project\\TextEditorProgram",
                                title="Open file",
                                filetypes=(("Text files","*.txt"),("All files","*.*")),
                                defaultextension=".txt")
    try:
        window.title(os.path.basename(file_path))
        file_path = open(file_path,"r")
        text_area.delete(1.0,"end")
        text_area.insert(1.0,file_path.read())
        file_path.close()
    except Exception:
        print("Couldn't read this file")

def save_file():
    file_path = filedialog.asksaveasfilename(initialdir="C:\\Users\\Acer\\PycharmProjects\\HelloWorld\\game_and_project\\TextEditorProgram",
                                  filetypes=(("Text files","*.txt"),("All file","*.*")),
                                  defaultextension=".txt",
                                  initialfile="Untitled.txt")
    if file_path is None:
        return
    else:
        try:
            window.title(os.path.basename(file_path))
            file_path = open(file_path,"w")
            file_path.write(text_area.get(1.0,"end"))
            file_path.close()
        except Exception:
            print("Couldn't save file")

def exit_win():
    window.destroy()

def copy_edit():
    text_area.event_generate("<<Copy>>")

def cut_edit():
    text_area.event_generate("<<Cut>>")

def paste_edit():
    text_area.event_generate("<<Paste>>")

def delete_edit():
    text_area.delete("sel.first","sel.last")

def undo_edit():
    text_area.edit_undo()

def redo_edit():
    text_area.edit_redo()

def select_edit():
    text_area.tag_add("sel","1.0","end")

def information_help():
    messagebox.showinfo(title="About text editor",message="This text editor program was written by Thinh on May 1st.")

def press(event):
    key = event.keysym
    if key == "n" or key == "N":
        new_file()
    elif key == "o" or key == "O":
        open_file()
    elif key == "s" or key == "S":
        save_file()
    elif key == "c" or key == "C":
        copy_edit()
    elif key == "x" or key == "X":
        cut_edit()
    elif key == "v" or key == "V":
        paste_edit()
    elif key == "a" or key == "A":
        select_edit()

# kích thước màn hình
WIDTH = 500
HEIGHT = 500

window = Tk()

# icon trong lệnh file_menu
image_newFile = ImageTk.PhotoImage(Image.open(os.path.join("assets","images","icons","new_file.png")))
image_openFile = ImageTk.PhotoImage(Image.open(os.path.join("assets","images","icons","open_file.png")))
image_saveFile = ImageTk.PhotoImage(Image.open(os.path.join("assets","images","icons","save_file.png")))
image_exitFile = ImageTk.PhotoImage(Image.open(os.path.join("assets","images","icons","exit_file.png")))
image_logo = ImageTk.PhotoImage(Image.open(os.path.join("assets","images","icons","TextEditor.png")))

# kích thước của màn hình desktop
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# vị trí window
x_window = (screen_width//2) - (WIDTH//2)
y_window = (screen_height//2) - (HEIGHT//2)
window.geometry("{}x{}+{}+{}".format(WIDTH,HEIGHT,x_window,y_window)) # thiết lập kích thước và vị trí của màn hình
# tên cửa sổ
window.title("Text editor")
window.iconphoto(True,image_logo)
# # logo cho window
# logo = PhotoImage(file="TextEditor.png")
# window.iconphoto(True,logo)

font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("25")

# tạo vùng để soạn thảo văn bản
text_area = Text(window,font=(font_name.get(),font_size.get()))
# tạo thanh cuộn
scroll_bar = Scrollbar(text_area,command=text_area.yview)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()
# button thay đổi màu chữ
color_button = Button(frame,text="Color",command=color_change)
color_button.grid(row=0,column=0)
# option thay đổi font chữ
font_option = OptionMenu(frame,font_name,*font.families(),command=font_change)
font_option.grid(row=0,column=1)
# option thay đổi cỡ chữ
size_option = Spinbox(frame,from_=1,to=100,textvariable=font_size,command=font_change)
size_option.grid(row=0,column=2)

scroll_bar.pack(side=RIGHT,fill=Y) # thanh cuộn ở bên phải và tự mở rộng theo chiều dọc để điền vào vùng cha nó(text_area) được đặt vào
text_area.config(yscrollcommand=scroll_bar.set)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New file",command=new_file,image=image_newFile,compound="left")
file_menu.add_command(label="Open file",command=open_file,image=image_openFile,compound="left")
file_menu.add_command(label="Save",command=save_file,image=image_saveFile,compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit_win,image=image_exitFile,compound="left")
# phím tắt để thao tác với file_menu
window.bind("<Control-KeyPress>",press)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Copy",command=copy_edit)
edit_menu.add_command(label="Cut",command=cut_edit)
edit_menu.add_command(label="Paste",command=paste_edit)
edit_menu.add_command(label="Delete",command=delete_edit)
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=undo_edit)
edit_menu.add_command(label="Redo",command=redo_edit)
edit_menu.add_separator()
edit_menu.add_command(label="Select all",command=select_edit)

help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About text editor program",command=information_help)


window.mainloop()