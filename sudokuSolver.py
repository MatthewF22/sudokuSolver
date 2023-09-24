#Created 9/24/2023 - Matthew Franklin
#This is a program that utilizes a backtracking algorithm in order to solve a sudoku board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#Function to actually print the board out in the correct format in the terminal
def print_board(theboard):
    #grab each list of the board ie. each row
    for i in range(len(theboard)):
        #Every third row we want to print a horizontal line to create a grid for our board
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(theboard[0])):
            #Checking inside the row, if we are at a position that is a multiple of 3 we want to draw vertical lines to continue creating that grid
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            #If we are at the end of the row then there is no need to print a space because we want a new line to start for the next row
            #If we are not at the end, use end="" so that there is not a newline created
            if j == 8:
                print(theboard[i][j])
            else:
                print(str(theboard[i][j])+" ", end="")

def find_empty(theboard):
    #First grab the row's or lists one by one
    for i in range(len(theboard)):
        #next, check each column value inside the row we just grabbed
        for j in range(len(theboard[i])):
            #this is taking the row and the column position, and if it is 0 or empty then we return the position because we are finding empty positions
            if theboard[i][j] == 0:
                return(i, j)
    #If there are no blank spaces return none
    return None

#Determine if the board we have is valid and can be solved by the rules of sudoku
def valid(theboard, num, pos):
    #Check the row
    for i in range(0, len(theboard[0])):
        if theboard[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(0, len(theboard)):
        if theboard[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 grid
    #These values will give us a 0, 1, or 2 to identify which row and column our box is
    box_x = pos[1] // 3
    box_y = pos[0] // 3


    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if theboard[i][j] == num and (i,j) != pos:
                return False

    return True


def solve(theboard):
    #Use find variable to identify empty positions on the board
    find = find_empty(theboard)
    #If we cant find emplty positions then we have a complete board
    if not find:
        return True
    else:
        #find_empty return (row, col) so we gather that information here in variables row, col = find
        row, col = find
    #Check values 1-9 to see if they work as a solution in the current position
    for i in range(1,10):
        #check if the number i is a valid solution for our position on the board
        if valid(theboard, i, (row, col)):
            #If the number i is valid for the position, then add it to the board
            theboard[row][col] = i

            if solve(theboard):
                return True

            theboard[row][col] = 0

    return False

print(print_board(board))
solve(board)
print("Solved board below!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(print_board(board))

