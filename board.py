
# Get the current board status
def cur_board_status():
    print("to be added")

# Print the current board
def print_board(row,col,board):

    if row>0 and col>0 :
        print("---------")
        for r in range(row):
            for c in range(row):
                print(board[r][c]+" ",end=" ")
            print()   
        print("----------")
def board():
    rows,cols=(3,3)
    board=[]

    # Initialize the board with the default values
    for i in range(rows):
        col=[]
        for j in range(cols):
            col.append("%")
        board.append(col)

    print_board(rows,cols,board)        


board()
    