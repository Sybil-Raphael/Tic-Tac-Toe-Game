"""
Name: Sybil Raphael
Class: 1411-001
Due Date: November 15, 2023
Description: Practice using nested lists, nested loops,
f strings, and functions to create a game (tic-tac-toe)
Status: Run as expected
"""


def reset_grid(grid):
    for i in range(3):
        for j in range(3):
            grid[i][j] = ' '


def check_row (grid, row_num):
    if (grid[row_num][0]== 'x' and grid[row_num][1]== 'x' and grid[row_num][2]== 'x'):
        return True
    elif (grid[row_num][0]== 'o' and grid[row_num][1]== 'o' and grid[row_num][2]== 'o'):
        return True
    return False


def check_column (grid, col_num):
    if (grid[0][col_num]== 'x' and grid[1][col_num]== 'x' and grid[2][col_num]== 'x'):
        return True
    elif (grid[0][col_num]== 'o' and grid[1][col_num]== 'o' and grid[2][col_num]== 'o'):
        return True
    return False


def check_diagonal (grid, diagonal):
    if (diagonal == 'd1'):
        if (grid[0][0]== 'x' and grid[1][1]== 'x' and grid[2][2]== 'x'):
            return True
        elif (grid[0][0]== 'o' and grid[1][1]== 'o' and grid[2][2]== 'o'):
            return True
    else:
        if diagonal == 'd2':
            if (grid[0][2]== 'x' and grid[1][1]== 'x' and grid[2][0]== 'x'):
                return True
            elif (grid[0][2]== 'o' and grid[1][1]== 'o' and grid[2][0]== 'o'):
                return True

def place_entry (grid, row_num, col_num, ch):
    if (grid[row_num][col_num] == ' '):
        grid[row_num][col_num] = ch
        return True
    elif (grid[row_num][col_num] != ' '):
        return False


def playable (grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ' ':
                return True
    return False

    
def print_grid (grid):
    print('-------------')
    for x in range (3):
        for y in range (3):
            print(f'| {grid[x][y]:2s}', end='')
        print('|\n -------------')


def main():
    grid = [[' ', ' ', ' '], \
           [' ', ' ', ' '], \
           [' ', ' ', ' ']]

    new_game = 'y'

    while new_game == 'y':

        player1 = input('Player 1 (x) enter your name: ')
        player2 = input('Player 2 (o) enter your name: ')

        game_over = False


        while game_over == False:
            row_num, col_num = input(f'{player1} enter location to be marked (row, col): ').split()
            row_num = int(row_num)
            col_num = int(col_num)

    
            if row_num >= 4 or col_num >= 4:
                print('Error: Your row or column number is out of bound')

            else:

                if place_entry (grid, row_num - 1, col_num - 1, 'x') == True:

                    print_grid(grid)
                    
                    if check_row (grid, row_num - 1) == True:
                        print(f'Congratulations {player1} you won!')
                        game_over = True
                        break 

                    if check_column (grid, col_num - 1) == True:
                        print(f'Congratulations {player1} you won!')
                        game_over = True
                        break

                    if check_diagonal (grid, 'd1') == True:
                        print(f'Congratulations {player1} you won!')
                        game_over = True
                        break

                    if check_diagonal (grid, 'd2') == True:
                        print(f'Congratulations {player1} you won!')
                        game_over = True
                        break

                    if playable (grid) == False:
                        print('The game is a draw')
                        break
                else:
                    print('Error: This cell is already taken')
         

            row_num, col_num = input(f'{player2} enter location to be marked (row, col): ').split()
            row_num = int(row_num)
            col_num = int(col_num)
    
            if row_num >= 4 or col_num >= 4:
                print('Error: Your row or column number is out of bound')
                
            else:

                if place_entry (grid, row_num - 1, col_num - 1, 'o') == True:
                    print_grid(grid)
                    
                    if check_row (grid, row_num - 1) == True:
                        print(f'Congratulations {player2} you won!')
                        game_over = True
                        break 

                    if check_column (grid, col_num - 1) == True:
                        print(f'Congratulations {player2} you won!')
                        game_over = True
                        break

                    if check_diagonal (grid, 'd1') == True:
                        print(f'Congratulations {player2} you won!')
                        game_over = True
                        break

                    if check_diagonal (grid, 'd2') == True:
                        print(f'Congratulations {player1} you won!')
                        game_over = True
                        break

                    if playable (grid) == False:
                        print('The game is a draw')
                        break
                else:
                    print('Error: This cell is already taken')

                print_grid(grid)
                    

        input('Do you want to play again (y or n)?')
        if 'y':
            reset_grid(grid)

                
        
            

        


