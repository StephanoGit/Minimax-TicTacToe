from tkinter import PhotoImage, Tk, Button, messagebox
import math

def create_buttons():
    for i in range(9):
        square[i] = Button(window, image=available_space, width="100", height="100",
                            command=lambda value=i:handle_button_click(value))

def square_taken():
    messagebox.showinfo("Square Taken", "Square already taken choose another!")

def checkdraw():
    for i in range(3):
        for j in range(3):
            if oxo[i][j] == ' ':
                return False
    return True

def checkwin(mark):
    won = []
    won.append(oxo[0][0] == oxo[1][1] == oxo[2][2] and oxo[0][0] != mark)
    won.append(oxo[0][2] == oxo[1][1] == oxo[2][0] and oxo[0][2] != mark)

    for i in range(3):
        won.append(oxo[i][0] == oxo[i][1] == oxo[i][2] and oxo[i][0] != mark)
        won.append(oxo[0][i] == oxo[1][i] == oxo[2][i] and oxo[0][i] != mark)
    
    if True in won:
        # button = Button(window, image=winner, width="300", height="100")
        # button.pack()
        return True

    return False

def update_move(square_number, player_number):
    square_to_oxo_map = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    m = square_to_oxo_map
    p = player_number
    s = square_number
    oxo[m[s][0]][m[s][1]] = p
    checkwin(" ")
    checkdraw()

def handle_button_click(button_number):
    global counter
    square[button_number].configure(image=player1_taken, command=square_taken)
    update_move(button_number, 1)
    bestMove()


def minimax(board, depth, isMaximizing):
    if checkwin(2):
        return 1
    elif checkwin(1):
        return -1
    elif checkdraw():
        return 0

    if isMaximizing:
        bestScore  = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 2
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    if score > bestScore:
                        bestScore = score

        return bestScore

    else:
        bestScore  = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 1
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    if score < bestScore:
                        bestScore = score

        return bestScore


def bestMove():
    global counter
    bestScore  = -1000
    move = [0, 0]

    for i in range(3):
        for j in range(3):
            if oxo[i][j] == " ":
                oxo[i][j] = 2
                score = minimax(oxo, 0, False)
                oxo[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move[0] = i
                    move[1] = j
    
    square[(move[0] * 3) + move[1]].configure(image=player2_taken, command=square_taken)
    update_move((move[0] * 3) + move[1], 2)

# CREATE WINDOW
window = Tk()

window.title("OXO Game")
window.geometry("300x300")

available_space = PhotoImage(file="images/myButton.png")
player1_taken = PhotoImage(file="images/myButtonP1.png")
player2_taken = PhotoImage(file="images/myButtonP2.png")
winner = PhotoImage(file="images/winner.png")


square = [None] * 9
create_buttons()
index = 0;
for i in range(3):
    for j in range(3):
        square[index].place(x=i*100, y=j*100)
        index += 1

counter = 0

oxo = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]



# DISPLAY WINDOW
window.mainloop()