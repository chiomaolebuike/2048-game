# Program that push values up, down, left and right
# Chioma Olebuike
# 17 April 2024

import util

def push_up(grid): # problem
    """merge grid values upwards""" 
    new_grid = grid
    # Shift non-zero values upwards
    for c in range(4):
        col_values = [new_grid[r][c] for r in range(4) if new_grid[r][c] != 0]
        for r in range(4):
            new_grid[r][c] = col_values[r] if r < len(col_values) else 0
    
    for c in range(4):
        merged = [False, False, False, False]
        for r in range(1, 4):  # Start from the second row since the first row can't move up
            if new_grid[r][c] != 0:  # If the current cell is not empty
                i = r
                while i > 0:  # Loop from the current row towards the top
                    if new_grid[i-1][c] == 0:
                        new_grid[i-1][c] = new_grid[i][c]  # Shift up
                        new_grid[i][c] = 0
                        i -= 1  # Check the next cell above
                    elif (new_grid[i-1][c] == new_grid[i][c]) and not merged[i-1]:  # Merge if the cells are equal and not already merged
                        new_grid[i-1][c] *= 2
                        new_grid[i][c] = 0
                        merged[i-1] = True
                        break  # Move to the next cell after merging
                    else:
                        break  # No merge or move is possible
#Shift zeros upwards again
    for c in range(4):
        col_values = [new_grid[r][c] for r in range(4) if new_grid[r][c] != 0]
        for r in range(4):
            new_grid[r][c] = col_values[r] if r < len(col_values) else 0
        

def push_down(grid):
    """Merge grid values downwards"""
    new_grid = grid
    for c in range(4):
        col_values = [new_grid[r][c] for r in range(3, -1, -1) if new_grid[r][c] != 0]
        for r in range(3, -1, -1):
            new_grid[r][c] = col_values[3 - r] if 3 - r < len(col_values) else 0

    for c in range(4):
        merged = [False, False, False, False]
        for r in range(2, -1, -1):  # Start from the second-to-last row (row 3) and move downwards
            if new_grid[r][c] != 0:  # If the current cell is not empty
                i = r
                while i < 3:  # Loop from the current row downwards to the bottom
                    if new_grid[i+1][c] == 0:
                        new_grid[i+1][c] = new_grid[i][c]  # Shift down
                        new_grid[i][c] = 0
                        i += 1  # Check the next cell below
                    elif (new_grid[i+1][c] == new_grid[i][c]) and not merged[i+1]:  # Merge if the cells are equal and not already merged
                        new_grid[i+1][c] *= 2
                        new_grid[i][c] = 0
                        merged[i+1] = True
                        break  # Move to the next cell after merging
                    else:
                        break  # No merge or move is possible
    for c in range(4):
        col_values = [new_grid[r][c] for r in range(3, -1, -1) if new_grid[r][c] != 0]
        for r in range(3, -1, -1):
            new_grid[r][c] = col_values[3 - r] if 3 - r < len(col_values) else 0

   

def push_left (grid): # problem
    """merge grid values left""" 
    new_grid = grid                       
    
    for r in range(4):
        row_values = [val for val in new_grid[r] if val != 0]
        new_grid[r] = row_values + [0] * (4 - len(row_values))
           
    for r in range(4):
        merged = [False,False,False,False] 
        for c in range(1, 4):  # start from last column to the second column, col 0 most left
            if new_grid[r][c] != 0:  # if the current cell is not empty
                i = c
                while i > 0:  # loop from current column towards the left
                    if new_grid[r][i-1] == 0:
                        new_grid[r][i-1] = new_grid[r][i]  # shift left
                        new_grid[r][i] = 0  
                        i -= 1  # checking the next cell above
                    elif (new_grid[r][i-1] == new_grid[r][i]) and not merged[i-1]:  # merge if the cells are equal and not already merged
                        new_grid[r][i-1] *= 2
                        new_grid[r][i] = 0 
                        merged[i-1] = True  
                        break  # move to the next cell after merging
                    else:
                        break  # no merge or move is possible
                    
    for r in range(4):
        row_values = [val for val in new_grid[r] if val != 0]
        new_grid[r] = row_values + [0] * (4 - len(row_values))                    
 
                    
def push_right (grid):  # across cols
    """merge grid values right"""
    new_grid = grid
    for r in range(4):
            row_values = [val for val in new_grid[r] if val != 0]
            new_grid[r] = [0] * (4 - len(row_values)) + row_values
            
    for r in range(4):
        merged = [False, False, False, False]
        for c in range(2, -1, -1):  # Start from the second-to-last column (column 3) and move left
            if new_grid[r][c] != 0:  # If the current cell is not empty
                i = c
                while i < 3:  # Loop from the current column to the right
                    if new_grid[r][i+1] == 0:
                        new_grid[r][i+1] = new_grid[r][i]  # Shift right
                        new_grid[r][i] = 0
                        i += 1  # Check the next cell above
                    elif (new_grid[r][i+1] == new_grid[r][i]) and not merged[i+1]:  # Merge if the cells are equal and not already merged
                        new_grid[r][i+1] *= 2
                        new_grid[r][i] = 0
                        merged[i+1] = True
                        break  # Move to the next cell after merging
                    else:
                        i += 1  # Check the next cell to the right
                        
    for r in range(4):
        row_values = [val for val in new_grid[r] if val != 0]
        new_grid[r] = [0] * (4 - len(row_values)) + row_values
    

# Now you have a push_right function based on the same principles as your push_left function

    