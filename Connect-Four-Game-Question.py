'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 | 0,6
  1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6
  2,0 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5 | 2,6
  3,0 | 3,1 | 3,2 | 3,3 | 3,4 | 3,5 | 3,6
  4,0 | 4,1 | 4,2 | 4,3 | 4,4 | 4,5 | 4,6
  5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5 | 5,6
'''
N, M = 6, 7
grid = [['.'for x in range(M)]for y in range(N)]

#This function prints the grid of Connect Four Game as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win(mark,i):
    for j in range(7):
        if grid[j][i]=='.':
            continue
        else :
            break
    if 0<=j<=2:
        if grid[j+1][i]==grid[j+2][i]==grid[j+3][i]==mark:
          return True
    
    co=0
    for l in range(i,-1,-1):
        if grid[j][l]== mark:
            co+=1
        else :
            break
    for r in range(i+1,7):
        if grid[j][r]== mark:
            co+=1 
        else :
            break
    if co>=4: 
        return True

    co1=0
    a,y=j,i
    while j<=a<6 and i<=y<7:
        if grid[a][y]== mark:
            co1+=1
        else :
            break
        a+=1
        y+=1
    f,x=j-1,i-1
    while -1< f <j and -1< x <i :    
        if grid[f][x]== mark:
            co1+=1
        else :
            break
        f-=1
        x-=1
    if co1>=4: 
        return True
    
    co2=0
    a,y=j,i
    while a<6 and -1<y :
        if grid[a][y]== mark:
            co2+=1
        else :
            break
        a+=1
        y-=1
    f,x=j-1,i+1
    while -1<f and  x<7 :    
        if grid[f][x]== mark:
            co2+=1
        else :
            break
        f-=1
        x+=1
    if co2>=4: 
        return True
    return False
#This function checks if row or column or diagonal is full with same characters
def check_tie():
    d=0
    for i  in range(N):
        for j in range(M):
            if grid[i][j]!='.':
                d+=1
    if d == N*M:
        return True
    else:
        return False  

#This function checks if given cell is empty or not 
def check_empty(i):
    h = (grid[0][i]=='.')
    return h

#This function checks if given position is valid or not 
def check_valid_column(i):
    t = (0<=i<7)
    return t

#This function sets a value to a cell
def set_cell(i, mark):
    for j in range(5,-1,-1):
       if grid[j][i]=='.':
        grid[j][i]=mark
        break

#This function clears the grid
def grid_clear():
    global grid
    grid = [['.'for x in range(M)]for y in range(N)]
    

#MAIN FUNCTION
def play_game():
    print("Connect Four Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Takes input from the user to fill in the grid
        print('Player %s' % mark)
        i = int(input('Enter the column index: '))
        i-=1
        while not check_valid_column(i) or not check_empty(i):
            i = int(input('Enter a valid column index: '))
            i-=1
        #Set the input position with the mark
        set_cell(i, mark)
        #Check if the state of the grid has a win state
        #op_mark = 'O' if player == 0 else 'X'
        if check_win(mark,i):
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        #Check if the state of the grid has a tie state
        if check_tie():
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break		
        #Player number changes after each turn
        player = 1 - player 


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
