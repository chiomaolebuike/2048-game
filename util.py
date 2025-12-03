# Program to write module of utility functions
# Chioma Olebuike
# 14 April 2024

# util.py

def create_grid(grid):
    """Create a 4x4 array of zeroes within grid"""
    for i in range(4):
        grid.append([0] * 4)
    return grid

def print_grid(grid):
    """Print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in grid:
        print("|", end="")
        for cell in row: # left justify
            if cell == 0:
                print("{:<5}".format(''), end="")
            else:
                print("{:<5}".format(cell), end="")
        print("|")
    print("+--------------------+")
       

def check_lost(grid):
    """return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0 :
                return False
            if i < 3 and grid[i][j] == grid[i+1][j]:
                return False
            if j < 3 and grid[i][j] == grid[i][j+1]:
                return False
    return True

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    return False

def copy_grid(grid): # deep copy
    """return a copy of the given grid"""
    new_grid = []
    create_grid(new_grid)
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][j]
    return new_grid


def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True


'''def main():
    grid = []
    create_grid(grid)
    print_grid(grid)
    print(check_lost(grid))
    print(check_won(grid))
    print(copy_grid(grid))
    
    
if __name__ == '__main__':
    main() '''