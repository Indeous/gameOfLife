import sys
import os

def grid_dim(grid):
    '''calculate length of grid (why and addition function?)'''
    return len(grid[0]), len(grid)
    
def read_grid(file_path):
    
    with open(file_path) as f:
        w, h = None, None
        grid = []
        
        for line in f:
            x, y = map(int, line.split())
            if w is None and h is None:
                w, h = y, x
                for i in range(h):    
                    # h is no. of rows, this initialises an staring board with zeros
                    grid.append([0] * w)    
                    # list comprehension, [0] * w gives list with w 0s
            else:
                grid[x-1][y-1] = 1    
                # assigns 1 to desired cells (but doesn't python count rows and columns from 0?)
                # yes, IndexError can occur. input.txt should contain first w, h 
                # and indices of active cells counding from zero
                # to correct for this -1 on x and y indices
    return grid


# def tick(grid):
    # to work on

def main():
    # print(sys.argv) # gives a list of arg that are given while running game.py
    
    try:
        input_name = sys.argv[1]
    except IndexError:
        # we want to except only IndexError so we specify it
        sys.exit("No input filename.")
        #sys.exit() is used within a program, exit() is used for interactive shells
    try:
        output_name = sys.argv[2]
    except IndexError:
        sys.exit("No output filename.")
        
    # try
    # if not (len(input_name.split('.')) == 2) and (len(output_name.split('.')) == 2) and (input_name.split('.')[1] == 'txt') and (output_name.split('.')[1] == 'txt'):
    # except IndexError:
        # sys.exit("Invalid input or output filename. Should be __.txt format.")
    # tried to validate input output names
    
    try:
        n = int(sys.argv[3])
    except IndexError: 
        sys.exit("No number of generations.")
    except ValueError: 
        sys.exit("Invalid number of generations {}.".format(sys.argv[3]))
    
    # print(input_name,output_name,n)
    
    grid = read_grid(input_name)
    # print (grid)
    
    dim = grid_dim(grid)
    # print(dim)
    
    
if __name__ == "__main__":
    main()