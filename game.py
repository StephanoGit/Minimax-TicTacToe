from tkinter import PhotoImage, Tk, Button

def create_bttns():
    for i in range(9):
        squares[i] = Button(window,image=available_space, width="145", height="145",
                            command=lambda value=i:handle_button_click(value),
                            borderwidth=0, highlightthickness=0, highlightcolor="#5A3392")

def checkdraw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def checkwin():
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != " "):
        return True
    if (board[0][2] == board[1][1] == board[2][0] and board[0][2] != " "):
        return True

    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] and board[i][0] != " "):
            return True
        if (board[0][i] == board[1][i] == board[2][i] and board[0][i] != " "):
            return True

    return False

def checkwin2(symbol):
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] == symbol):
        return True
    if (board[0][2] == board[1][1] == board[2][0] and board[0][2] == symbol):
        return True

    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] and board[i][0] == symbol):
            return True
        if (board[0][i] == board[1][i] == board[2][i] and board[0][i] == symbol):
            return True

    return False

def update_move(square_number, symbol):
    square_to_board_map = [[0, 0], [0, 1], [0, 2],
                           [1, 0], [1, 1], [1, 2],
                           [2, 0], [2, 1], [2, 2]]
    m = square_to_board_map
    s = square_number
    board[m[s][0]][m[s][1]] = symbol

    checkwin()
    checkdraw()

def minimax(board, depth, isMaximizing):
    if checkwin2(bot):
        return 1
    elif checkwin2(player):
        return -1
    elif checkdraw():
        return 0

    if isMaximizing:
        bestScore  = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = bot
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    if score > bestScore:
                        bestScore = score

        return bestScore

    else:
        bestScore  = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    if score < bestScore:
                        bestScore = score

        return bestScore

def checkBestMove():
    bestScore  = -1000
    moveX = 0
    moveY = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = bot
                score = minimax(board, 2, False)
                if score > bestScore:
                    bestScore = score
                    moveX = i
                    moveY = j
                board[i][j] = " "
    
    squares[(moveX * 3) + moveY].configure(image=player2_taken)
    update_move((moveX * 3) + moveY, bot)


def handle_button_click(button_number):

    if checkwin() == False:
        # Do player move
        squares[button_number].configure(image=player1_taken)
        update_move(button_number, player)

        # Do bot move
        checkBestMove()


window = Tk()

window.title("OXO Game")
window.geometry("435x435")
window.configure(background="#5A3392")

available_space = PhotoImage(file="images/empty.png")
player1_taken = PhotoImage(file="images/player1.png")
player2_taken = PhotoImage(file="images/player2.png")

counter = 0
squares = [None] * 9
create_bttns()

index = 0
for i in range(3):
    for j in range(3):
        squares[index].place(x=j*145, y=i*145)
        index += 1

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

player = "x"
bot = "o"

window.mainloop()