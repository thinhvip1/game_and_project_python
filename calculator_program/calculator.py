from tkinter import *
from PIL import ImageTk,Image
import os

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "(", ")", "."]
operators = ["+","-","*","/"]
# hàm để nhận thông tin khi ấn vào button
def button_click(key):
    global cal
    if cal == "" and key in operators:
        cal = f"0{key}"
    else:
        cal = cal + str(key)
    cal_var.set(cal)
# hàm để nhận thông tin khi nhấn bàn phím
def key_press(event):
    global cal
    # trả về kí tự mà phím được nhấn
    key = event.char
    # nếu chuỗi không rỗng và kí tự cuối của chuỗi không phải là toán tử và phím vừa bấm vào là chữ số và toán tử
    if cal == "" and key in operators:
        cal = f"0{key}"
    elif cal == "" and (key == "=" or event.keysym == "Return"):
        cal = "0"
    elif key in digits or key in operators:
        cal = cal + key
    elif key == "=" or event.keysym == "Return":
        equals()
        return
    cal_var.set(cal)

# hàm để đưa ra kết quả
def equals():
    global cal
    try:
        cal = str(eval(cal))
        cal_var.set(cal)
    except ZeroDivisionError:
        cal_var.set("Math error!")
    except SyntaxError:
        cal_var.set("Syntax error!")
# hàm để xóa từng kí tự từ cuối bằng cách click vào button
def backspace_click():
    global cal
    cal = cal[:-1]
    cal_var.set(cal)
# hàm để xóa từng kí tự từ cuối bằng cách ấn phím BackSpace
def backspace_press(event):
    backspace_click()
# hàm để xóa tất cả chuỗi trên thanh bằng cách click vào Button
def del_all():
    global cal
    cal = ""
    cal_var.set(cal)
# hàm để xóa tất cả chuỗi trên thanh bằng tổ hợp phím Shift + BackSpace
def backspace_all(event):
    del_all()

WINDOW_WIDTH = 430
WINDOW_HEIGHT = 665



window = Tk()
window.title("Calculator program")

# image
image_backspace = ImageTk.PhotoImage(Image.open(os.path.join("assets","images","buttons","delete.png")))
image_window = ImageTk.PhotoImage(Image.open(os.path.join("assets","images","icons","calculator.png")))

# kích thước và vị trí của window
x_window = (window.winfo_screenwidth()//2)-(WINDOW_WIDTH//2)
y_window = (window.winfo_screenheight()//2)-(WINDOW_HEIGHT//2)
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_window}+{y_window}")

window.iconphoto(True,image_window)

cal = "" # lưu phép tính
cal_var = StringVar()
label_cal = Label(window,textvariable=cal_var,font=("Arial",20),bg="#cadff1",width=25,height=2,relief=SUNKEN,bd=8)
label_cal.pack()

frame = Frame(window)
frame.pack()
# key number 1
button1 = Button(frame, text="1", width=8, height=4, font=35, command= lambda:button_click(1),relief=RAISED,bd=5)
button1.grid(row=0,column=0,padx=(0,1),pady=(1,0))
# key number 2
button2 = Button(frame, text="2", width=8, height=4, font=35, command= lambda:button_click(2),relief=RAISED,bd=5)
button2.grid(row=0,column=1,padx=(0,1),pady=(1,0))
# key number 3
button3 = Button(frame, text="3", width=8, height=4, font=35, command= lambda:button_click(3),relief=RAISED,bd=5)
button3.grid(row=0,column=2,padx=(0,1),pady=(1,0))
# key number 4
button4 = Button(frame, text="4", width=8, height=4, font=35, command= lambda:button_click(4),relief=RAISED,bd=5)
button4.grid(row=1,column=0,padx=(0,1),pady=(1,0))
# key number 5
button5 = Button(frame, text="5", width=8, height=4, font=35, command= lambda:button_click(5),relief=RAISED,bd=5)
button5.grid(row=1,column=1,padx=(0,1),pady=(1,0))
# key number 6
button6 = Button(frame, text="6", width=8, height=4, font=35, command= lambda:button_click(6),relief=RAISED,bd=5)
button6.grid(row=1,column=2,padx=(0,1),pady=(1,0))
# key number 7
button7 = Button(frame, text="7", width=8, height=4, font=35, command= lambda:button_click(7),relief=RAISED,bd=5)
button7.grid(row=2,column=0,padx=(0,1),pady=(1,0))
# key number 8
button8 = Button(frame, text="8", width=8, height=4, font=35, command= lambda:button_click(8),relief=RAISED,bd=5)
button8.grid(row=2,column=1,padx=(0,1),pady=(1,0))
# key number 9
button9 = Button(frame, text="9", width=8, height=4, font=35, command= lambda:button_click(9),relief=RAISED,bd=5)
button9.grid(row=2,column=2,padx=(0,1),pady=(1,0))
# key number 0
button0 = Button(frame, text="0", width=8, height=4, font=35, command= lambda:button_click(0),relief=RAISED,bd=5)
button0.grid(row=3,column=0,padx=(0,1),pady=(1,0))
# key AC
buttonAC = Button(frame,text="AC",width=8,height=4,font=35,command=del_all,relief=RAISED,bd=5)
buttonAC.grid(row=4,column=3,padx=(0,1),pady=(1,0))
# key (
button_open = Button(frame,text="(",width=8,height=4,font=35,command=lambda:button_click("("),relief=RAISED,bd=5)
button_open.grid(row=4,column=0,padx=(0,1),pady=(1,0))
# key )
button_open = Button(frame,text=")",width=8,height=4,font=35,command=lambda:button_click(")"),relief=RAISED,bd=5)
button_open.grid(row=4,column=1,padx=(0,1),pady=(1,0))
# key Backspace
button_backspace = Button(frame, image=image_backspace, width=90, height=103,font=70,command=backspace_click,relief=RAISED,bd=5)
button_backspace.grid(row=4,column=2,padx=(0,1),pady=(1,0))
# key .
button_decimal = Button(frame,text=".",width=8,height=4,font=35,command= lambda:button_click("."),relief=RAISED,bd=5)
button_decimal.grid(row=3,column=1,padx=(0,1),pady=(1,0))
# key +
button_plus = Button(frame, text="+", width=8, height=4, font=35, command= lambda:button_click("+"),relief=RAISED,bd=5)
button_plus.grid(row=0,column=3,padx=(0,1),pady=(1,0))
# key -
button_minus = Button(frame, text="-", width=8, height=4, font=35, command= lambda:button_click("-"),relief=RAISED,bd=5)
button_minus.grid(row=1,column=3,padx=(0,1),pady=(1,0))
# key *
button_multi = Button(frame, text="*", width=8, height=4, font=35, command= lambda:button_click("*"),relief=RAISED,bd=5)
button_multi.grid(row=2,column=3,padx=(0,1),pady=(1,0))
# key /
button_quotient = Button(frame, text="/", width=8, height=4, font=35, command= lambda:button_click("/"),relief=RAISED,bd=5)
button_quotient.grid(row=3,column=3,padx=(0,1),pady=(1,0))
# key =
button_equal = Button(frame,text="=",width=8,height=4,font=35,command=equals,relief=RAISED,bd=5)
button_equal.grid(row=3,column=2,padx=(0,1),pady=(1,0))

# keyboard event
frame.bind("<Key>", key_press) # bấm phím bất kỳ
frame.bind("<BackSpace>",backspace_press) # bấm phím BackSpace
frame.bind("<Shift-BackSpace>",backspace_all) # bấm tổ hợp phím Shift-BackSpace

frame.focus_set()

window.mainloop()