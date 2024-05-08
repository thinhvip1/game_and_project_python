from tkinter import *
import random
from PIL import ImageTk,Image
import os

GAME_WIDTH = 700 # chiều rộng khung game
GAME_HEIGHT = 700 # chiều cao khung game
SNAKE_COLOR = "#00FF00" # màu rắn
BODY_PARTS = 2 # chiều dài ban đầu rắn
space_size = 50 # kích thước 1 ô của rắn
speed = 150 # tốc độ rắn bò (tốc độ càng lớn thì rắn bò càng chậm)
FOOD_COLOR = "#f50202" # màu đồ ăn của rắn
BACKGROUND_COLOR = "#000000" # màu nền khung game
LEVEL = ["Easy","Medium","Hard"]
space_sizes = [25,50]

class Snake:

    def __init__(self):
        self.body = BODY_PARTS
        self.coordinates = []
        self.squares = []
        # random vị trí xuất hiện của rắn
        x_appearence = random.randint(0,(GAME_HEIGHT//space_size)-1)*space_size
        for i in range(0,BODY_PARTS):
            self.coordinates.append([x_appearence,0])
        for x, y in self.coordinates:
            square = canvas_game.create_rectangle(x,y,x+space_size,y+space_size,fill=SNAKE_COLOR,tags="snake")
            self.squares.append(square)

class Food:

    def __init__(self):
        x = random.randint(0,(GAME_WIDTH//space_size)-1) * space_size
        y = random.randint(0,(GAME_HEIGHT//space_size)-1) * space_size
        self.coordinates = [x,y]
        self.canvas_food = canvas_game.create_oval(x,y,x+space_size,y+space_size,fill=FOOD_COLOR,tags="food")

def next_turn(snake, food):
    x,y = snake.coordinates[0]

    if direction == "up":
        y -= space_size
    elif direction == "down":
        y += space_size
    elif direction == "right":
        x += space_size
    elif direction == "left":
        x -= space_size

    snake.coordinates.insert(0, (x,y)) # thêm phần mới của rắn vào đầu list tọa độ

    # tạo hcn mới cho phần mới thêm của rắn
    square = canvas_game.create_rectangle(x, y, x+space_size, y+space_size, fill=SNAKE_COLOR)
    snake.squares.insert(0, square) # thêm phần hcn mới của rắn vào list quản lý hình rắn

    # nếu ăn được food thì sẽ tạo ra food ở vị trí mới và tăng hình rắn thêm 1 ô
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label_score.config(text=f"Score:{score}")
        canvas_game.delete("food")
        food = Food()

    else: # giữ nguyên hình rắn
        del snake.coordinates[-1] # xóa phần cuối của rắn khỏi list tọa độ
        canvas_game.delete(snake.squares[-1]) # xóa phần hcn cuối cùng khỏi canvas trò chơi
        del snake.squares[-1] # xóa phần hcn cuối cùng của rắn khỏi list quản lý hình rắn

    if check_collisions(snake):
        for square in snake.squares:
            canvas_game.itemconfig(square,fill="grey")
        window.after(700,game_over)
    else:
        window.after(speed, next_turn, snake, food) # sau speed miliseconds sẽ gọi làm funct next_turn

# thay đổi hướng đi của rắn
def change_direction(event):
    global direction
    key = event.keysym
    if key == "w" or key == "Up":
        if direction != "down":
            direction = "up"
    elif key == "s" or key == "Down":
        if direction != "up":
            direction = "down"
    elif key == "a" or key == "Left":
        if direction != "right":
            direction = "left"
    elif key == "d" or key == "Right":
        if direction != "left":
            direction = "right"

# kiểm tra va chạm
def check_collisions(snake):
    x,y = snake.coordinates[0]
    # chạm viền trò chơi
    if x < 0 or x >= GAME_WIDTH: # chạm vào chiều rộng khung game (canvas_game)
        return True
    elif y < 0 or y >= GAME_HEIGHT: # chạm vào chiều cao của khung game (canvas_game)
        return True

    # tự chạm vào thân rắn
    # so sánh từ điểm thứ 2 đảm bảo không so sánh đầu rắn với chính nó
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# màn hình lúc kết thúc trò chơi
def game_over():
    canvas_game.delete(ALL)
    x = canvas_game.winfo_width()/2
    y = canvas_game.winfo_height()/2
    canvas_game_over = canvas_game.create_text(x, y, text="GAME OVER", font=("consolas",100),
                                               fill="red", tags="gameover")
    # thêm butotn vào canvas game khi trò chơi kết thúc
    button_re_window = canvas_game.create_window(x, y/2,window=button_restart)
    button_exit_window = canvas_game.create_window(x, y + y/2, window=button_exit)

def new_game():
    canvas_game.delete(ALL)
    frame_option.pack_forget()

    window.geometry("704x772+416+21")
    canvas_game.config(width=GAME_WIDTH,height=GAME_HEIGHT)
    window.update()

    # khởi tạo đối tượng rắn và thức ăn
    snake = Snake()
    food = Food()

    # bắt đầu trò chơi (rắn bắt đầu bò)
    next_turn(snake,food)

# sử dụng phím enter để chấp nhận chơi mới
def key_new_game(event):
    new_game()

# làm mới lại trò chơi
def restart():
    global score, direction, snake, food

    score = 0
    label_score.config(text=f"Score:{score}")
    direction = "down"

    # xóa hết các phần tử (widget) trên canvas_game
    canvas_game.delete(ALL)
    # khởi tạo lại đối tượng rắn và thức ăn mới
    snake = Snake()
    food = Food()
    # bắt đầu trò chơi mới
    next_turn(snake,food)

def game_exit():
    window.destroy()

# mouse events
def enter_mouse(event):
    button_restart.config(bg="white",fg="#00FF00")

def leave_mouse(event):
    button_restart.config(bg="blue",fg="black")

def change_mode(*args):
    global speed,space_size

    if current_level.get() == "Easy":
        speed = 150

    elif current_level.get() == "Medium":
        speed = 100

    elif current_level.get() == "Hard":
        speed = 50

    if current_space_size.get() == 25:
        space_size = 25
    elif current_space_size.get() == 50:
        space_size = 50

window = Tk()

# images
image_logo = PhotoImage(file=os.path.join("assets","images","icons","snake_game.png"))
image_score = PhotoImage(file=os.path.join("assets","images","icons","apple_scores.png"))

window.title("Snake game")
window.iconphoto(True,image_logo)
window.resizable(False,False) # không cho phép thay đổi kích thước cửa sổ

current_level = StringVar()
current_space_size = IntVar()
score = 0
direction = "down"

label_score = Label(window,text="Score:{}".format(score),
                    font=("consolas",40),fg="red",
                    image=image_score,compound="right")
label_score.pack()
canvas_game = Canvas(window,width=GAME_WIDTH,height=GAME_HEIGHT,bg=BACKGROUND_COLOR,
                     borderwidth=2,relief=SOLID,highlightbackground="red")
canvas_game.pack()

# frame để chọn mode như level, space size
frame_option = Frame(canvas_game, width=GAME_WIDTH+label_score.winfo_width(),bg="black",
                     height=GAME_HEIGHT+label_score.winfo_height())
frame_option.pack()

label_level = Label(frame_option,text="Level:",font=("consolas,30"),width=10,height=2,bg="black",fg="#00FF00")
label_level.grid(row=0,column=0,padx=(GAME_WIDTH//4,0),pady=(GAME_HEIGHT//2,0))
# lựa chọn level
current_level.set("Easy")
option_level = OptionMenu(frame_option,current_level,*LEVEL,command=change_mode)
option_level.config(bg="black",fg="#00FF00",relief=RAISED)
option_level.grid(row=0,column=1,padx=(0,GAME_WIDTH//4),pady=(GAME_HEIGHT//2,0))

label_space_size = Label(frame_option,text="Space size:",font=("consolas,30"),bg="black",fg="#00FF00")
label_space_size.grid(row=1,column=0,padx=(GAME_WIDTH//4,0),pady=(0,GAME_HEIGHT//4))
# lựa chọn space size
current_space_size.set(space_size)
option_space_size = OptionMenu(frame_option,current_space_size,*space_sizes,command=change_mode)
option_space_size.config(bg="black",fg="#00FF00",relief=RAISED)
option_space_size.grid(row=1,column=1,padx=(0,GAME_WIDTH//4),pady=(0,GAME_HEIGHT//4))
# window["bg"] = "black"

window.update()

# set kích thước cũng như vị trí xuất hiện của window trên màn hình desktop
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth() # chiều rộng màn hình desktop
screen_height = window.winfo_screenheight() # chiều cao màn hình desktop
# tọa độ xuất hiện của window
x_window = (screen_width//2) - (window_width//2)
y_window = (screen_height//2) - (window_height//2)-25
window.geometry(f"{window_width}x{window_height}+{x_window}+{y_window}")

# thay đổi hướng đi của rắn
window.bind("<KeyPress>",change_direction)
window.bind("<Return>",key_new_game)
window.bind("<Enter>",enter_mouse) # chuột đi vào widget
window.bind("<Leave>",leave_mouse) # chuột rời khỏi widget

# khởi tạo button trên canvas_game để restart trò chơi
button_restart = Button(canvas_game, text="Restart", font=("consolas", 25), bg="blue",
                        width=20, height=2, command=restart)
# khởi tạo button trên canvas_game để thoát trò chơi
button_exit = Button(canvas_game, text="Exit", font=("consolas", 25), bg="blue",
                         width=20, height=2, command=game_exit)


# khởi tạo button trên frame_option để bắt đầu trò chơi
button_new = Button(canvas_game,text="New game", font=("consolas",25), bg="blue",
                    width=20, height=2,
                    command=new_game)
canvas_new = canvas_game.create_window(canvas_game.winfo_width()//2,
                                       canvas_game.winfo_height()//2-200,
                                       window=button_new)


# khởi tạo đối tượng rắn và thức ăn
# snake = Snake()s
# food = Food()

# bắt đầu trò chơi (rắn bắt đầu bò)
# next_turn(snake,food)

window.mainloop()