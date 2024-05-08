from tkinter import *
import random

'''
    Quy luật trò chơi: Người chơi thứ nhất sẽ được random 1 trong 2 lựa chọn X và O và tại mỗi lượt người chơi
chọn vào ô muốn đánh. Người chiến thắng sẽ là người có 3 ô thẳng hàng (3 ô thẳng cột, 3 ô chéo) trước hoặc nếu
không còn chỗ đánh mà chưa có ai thắng thì người chơi sẽ hòa nhau
'''
ROWS = 3
COLUMNS = 3
# kiểm tra xem lượt hiện tại của ai
def next_turn(row,column):
    global current_player
    if buttons[row][column]["text"] == "" and check_winner() == False:
        if current_player == players[0]:
            buttons[row][column].config(text=players[0],fg="red")

            if check_winner() == True: # thắng
                label_turn.config(text=current_player + " win",fg="red")
            elif check_winner() == None: # hòa
                label_turn.config(text=players[0]+players[1]+" draw!",fg="#d1cc6b")
            else: # tiếp tục
                current_player = players[1]
                label_turn.config(text=current_player + " turn",fg="blue")

        else:
            buttons[row][column].config(text=players[1],fg="blue")

            if check_winner() == True: # thắng
                label_turn.config(text=current_player + " win",fg="blue")
            elif check_winner() == None: # hòa
                label_turn.config(text=players[0]+players[1]+" draw!",fg="#d1cc6b")
            else: # tiếp tục
                current_player = players[0]
                label_turn.config(text=current_player + " turn",fg="red")

# kiểm tra xem người vừa đánh đã thắng chưa hoặc đã hòa chưa
def check_winner():
    # kiểm tra 3 ô thẳng hàng
    for row in range(ROWS):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            for column in range(COLUMNS):
                buttons[row][column].config(bg="#00FF00")
            return True
    # kiểm tra 3 ô thẳng cột
    for column in range(COLUMNS):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            for row in range(ROWS):
                buttons[row][column].config(bg="#00FF00")
            return True

    # kiểm tra 3 ô chéo nhau
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="#00FF00")
        buttons[1][1].config(bg="#00FF00")
        buttons[2][2].config(bg="#00FF00")
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="#00FF00")
        buttons[1][1].config(bg="#00FF00")
        buttons[2][0].config(bg="#00FF00")
        return True

    # kiểm tra xem còn ô trống không
    if empty_spaces() == False:
        for row in range(ROWS):
            for column in range(COLUMNS):
                buttons[row][column].config(bg="#d1cc6b")
        return None

    # chưa có ai thắng hoặc hòa
    return False

# kiểm tra xem trong bảng còn ô nào trống không nếu còn trả về True, không còn trả về False
def empty_spaces():
    # kiểm tra xem còn ô trống không nếu không còn trả về False
    spaces = 9
    for row in range(ROWS):
        for column in range(COLUMNS):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

# restart lại trò chơi
def new_game():
    global current_player
    current_player = random.choice(players) # reset lượt của người đánh đầu tiên
    label_turn.config(text=current_player+" turn",
                      fg="red" if current_player == players[0] else "blue",relief=RAISED) # reset label_turn
    # reset lại bảng
    for row in range(ROWS):
        for column in range(COLUMNS):
            # buttons[row][column]["text"] = ""
            buttons[row][column].config(text="",bg="SystemButtonFace")

window = Tk()
window.title("Tic-Tac-Toe")
window["bg"]="#4be3d4"
screen_width = window.winfo_screenwidth() # lấy ra chiều ngang của màn hình
screen_height = window.winfo_screenheight() # lấy ra chiều dọc của màn hình
# window_width = window.winfo_width() # lấy ra chiều ngang của cửa sổ window
# window_height = window.winfo_height() # lấy ra chiều dọc của cửa sổ window
# công thức tính tọa độ để cửa sổ xuất hiện ở giữa màn hình
x_window = screen_width//2 - 500//2
y_window = screen_height//2 - 500//2
window.geometry("{}x{}+{}+{}".format(500,500,x_window,y_window))

players = ["x","o"] # đại diện cho 2 người chơi
current_player = random.choice(players) # trả về 1 lựa chọn ngẫu nhiên trong list players
label_turn = Label(window,text=current_player+" turn",font=("Terminal",40),
                   fg="red" if current_player == players[0] else "blue",relief=RAISED)
label_turn.pack(side="top",pady=(7,0))
label_restart = Button(window,text="Restart",font=("Terminal",30),command=new_game,relief=RAISED)
label_restart.pack(side="top",pady=(7,7))

# tạo bảng
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
frame_table = Frame(window)
frame_table.pack(side="top")
for row in range(ROWS):
    for column in range(COLUMNS):
        buttons[row][column] = Button(frame_table,text="",font=("Terminal",20),width=7,height=4,
                        command= lambda row_click=row,column_click=column:next_turn(row_click,column_click))
        buttons[row][column].grid(row=row,column=column)


window.mainloop()