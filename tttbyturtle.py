#Code to perform a Tic-Tac-Toe game through Turtle
import turtle
import time
turtle.bgcolor('black')
turtle.title('Tic-Tac-Toe')
t = turtle.Turtle()
t.pensize(10)
s=turtle.Turtle()
s.color('red')
s.penup()
s.goto((0,-350))
s.hideturtle()
s.write("Welcome To the Game", font=("Arial", 16, "normal"),align='center')
time.sleep(3)
pos=[(-250,250),(-50,250),(150,250),(-250,50),(-50,50),(150,50),(-250,-150),(-50,-150),(150,-150)]
def cross_board():
    t.color('white')
    t.hideturtle()
    #for top sidewise
    t.penup()
    t.goto(-350,150)
    t.pendown()
    t.fd(600)
    #for right upward
    t.penup()
    t.rt(90)
    t.goto(50,-250)
    t.pendown()
    t.bk(600)
    #for down sidewise
    t.penup()
    t.lt(90)
    t.goto(250,-50)
    t.pendown()
    t.bk(600)
    #for left downward
    t.penup()
    t.rt(90)
    t.goto(-150,350)
    t.pendown()
    t.fd(600)
    
def x_mark(n1):
    t.color('red')
    t.penup()
    t.goto(pos[n1-1])
    t.goto(pos[n1-1][0]+50,pos[n1-1][1]+50)
    t.pendown()
    t.goto(pos[n1-1][0]-50,pos[n1-1][1]-50)
    t.penup()
    t.goto(pos[n1-1][0]-50,pos[n1-1][1]+50)
    t.pendown()
    t.goto(pos[n1-1][0]+50,pos[n1-1][1]-50)

def o_mark(n1):
    t.color('skyblue')
    t.penup()
    t.goto(pos[n1-1][0]-50,pos[n1-1][1])
    t.pendown()
    t.circle(50,360)
    

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']  #making a board
condition=True
cross_board()
#for marking X in board
def o_marking(n1):
    global board
    if n1>9 or n1<1:
        s.undo()
        s.write(f"Invalid input", font=("Arial", 16, "normal"),align="center")
        s.undo()
        num=turtle.numinput("Error Handle", "Enter a new number to mark with O:")
        s.write(f"{name1} entered: {int(num)}", font=("Arial", 16, "normal"),align="center")
        return o_marking(int(num))
    elif board[n1-1]=='O':
        s.undo()
        s.write(f"{name1} already take this position", font=("Arial", 16, "normal"))
        num=turtle.numinput("Error Handle", "Enter a new number to mark with O:")
        s.undo()
        s.write(f"{name1} entered: {int(num)}", font=("Arial", 16, "normal"),align="center")
        return o_marking(int(num))
    elif board[n1-1]=='X':
        s.undo()
        s.write(f"{name2} already take this position", font=("Arial", 16, "normal"))
        num=turtle.numinput("Error Handle", "Enter a new number to mark with O:")
        s.undo()
        s.write(f"{name1} entered: {int(num)}", font=("Arial", 16, "normal"),align="center")
        return o_marking(int(num))
    else:
        board[n1-1]='O'
        o_mark(n1)
        #print(' '+'|'.join(board[:3]),'\n','|'.join(board[3:6]),'\n','|'.join(board[6:]))

#for marking X in board
def x_marking(n2):
    global board
    if n2>9 or n2<1:
        s.undo()
        ss.write(f"Invalid input", font=("Arial", 16, "normal"),align="center")
        num=turtle.numinput("Error Handle", "Enter a new number to mark with X:")
        s.undo()
        s.write(f"{name1} entered: {int(num)}", font=("Arial", 16, "normal"),align="center")
        return x_marking(int(num))
    elif board[n2-1]=='O':
        s.undo()
        s.write(f"{name1} already take this position", font=("Arial", 16, "normal"),align='center')
        num=turtle.numinput("Error Handle", "Enter a new number to mark with O:")
        s.undo()
        s.write(f"{name1} entered: {int(num)}", font=("Arial", 16, "normal"),align="center")
        return x_marking(int(num))
    elif board[n2-1]=='X':
        s.undo()
        s.write(f"{name2} already take this position", font=("Arial", 16, "normal"))
        num=turtle.numinput("Error Handle", "Enter a new number to mark with O:")
        s.undo()
        s.write(f"{name1} entered: {int(num)}", font=("Arial", 16, "normal"),align="center")
        return x_marking(int(num))
    else:
        board[n2-1]='X'
        x_mark(n2)
        #print(' '+'|'.join(board[:3]),'\n','|'.join(board[3:6]),'\n','|'.join(board[6:]))


def winner():
    global board
    global condition
    if board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O':
        print(name1,'Won the Match')
        style = ("Arial", 24, "bold")
        s.undo()
        s.write(name1.capitalize()+" Won the Match", font=style, align="center")
        condition=False
    elif board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O':
        print(name1,'Won the Match')
        style = ("Arial", 24, "bold")
        s.undo()
        s.write(name1.capitalize()+" Won the Match", font=style, align="center")
        condition=False
    elif board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
        print(name1.capitalize(),'Won the Match')
        style = ("Arial", 24, "bold")
        s.undo()
        s.write(name1+" Won the Match", font=style, align="center")
        condition=False

    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X':
        print(name2,'Won the Match')
        style = ("Arial", 24, "bold")
        s.undo()
        s.write(name2.capitalize()+" Won the Match", font=style, align="center")
        condition=False
    elif board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X':
        print(name2,'Won the Match')
        style = ("Arial", 24, "bold")
        s.undo()
        s.write(name2.capitalize()+" Won the Match", font=style, align="center")
        condition=False
    elif board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
        print(name2,'Won the Match')
        style = ("Arial", 24, "bold")
        s.undo()
        s.write(name2.capitalize()+" Won the Match", font=style, align="center")
        condition=False
        
    #Draw condition
    if ' ' not in board and condition:
        print('Match is Draw')
        style = ("Arial", 24, "bold")
        s.undo()
        s.write("Match is Draw", font=style, align="center")
        condition=False

#giving names
name1=turtle.textinput("Person-1", "Enter your name:")
name2=turtle.textinput("Person-2", "Enter your name:")
print(' '+'|'.join(['1','2','3']),'\n','|'.join(['4','5','6']),'\n','|'.join(['7','8','9']))

#Main Game Loop
while condition:
    num = turtle.numinput("Number Prompt", "Enter a number to mark with O:")
    # Write it
    s.undo()
    s.write(f"{name1} entered: {int(num)}", font=("Arial", 16, "normal"),align="center")
    o_marking(int(num))
    winner()
    if condition==False:   #termination condition
        break

    num = turtle.numinput("Number Prompt", "Enter a number to mark with X:")
    # Write it
    s.undo()
    s.write(f"{name2} entered: {int(num)}", font=("Arial", 16, "normal"),align="center")
    x_marking(int(num))
    winner()
    if condition==False:   #termination condition
        break
time.sleep(3)
turtle.done()
