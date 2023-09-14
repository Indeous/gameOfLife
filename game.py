import sys
# import os  why specifically os.path?
import os.path
import random
import time

def grid_dim(grid):
    '''calculate length of grid (why an addition function?)'''
    return len(grid[0]), len(grid)
    
def read_grid(file_path):
    
    with open(file_path) as f:
        # w, h = None, None    < removed this
        
        try:
            h, w = map(int, f.readline().split())
        except ValueError:
            sys.exit("Invalid grid dimentions. Must be two unsigned integer values separated by a space.")
        
        grid = []
        for i in range(h):    
            # h is no. of rows, this initialises an staring board with zeros
            grid.append([0] * w)
            # list comprehension, [0] * w gives list with w 0s
        
        for line in f:
            x, y = map(int, line.split())
            grid[x][y] = 1    
            # assigns 1 to desired cells but python counts rows and columns from 0
            # to correct for this -1 can be added on x and y indices
            
            #learn and include input methods and y/n from agata
            
    return grid

def save_grid(grid,output_path):
    with open (output_path, "w") as f:
        w, h = grid_dim(grid)
        f.write(f"{h} {w}\n")    #str format {variable} and \n esc next line
        for y, row in enumerate(grid):    # y is row index starting from 0
            for x, cell in enumerate(row):
                if cell:
                    f.write(f"{y} {x}\n")    # x is column index starting from 0
    # no need to return as it writes on .txt already

def tick(grid):
    w, h = grid_dim(grid)

    temp = grid.copy()
    temp = [([0] * w) for y in range(h)]
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            count = 0
            if y > 0:
                count += grid[y - 1][x - 1] if x > 0 else 0
                count += grid[y - 1][x]
                count += grid[y - 1][x + 1] if x < w - 1 else 0

            count += grid[y][x - 1] if x > 0 else 0
            count += grid[y][x + 1] if x < w - 1 else 0
            
            if y < h - 1:
                count += grid[y + 1][x - 1] if x > 0 else 0
                count += grid[y + 1][x]
                count += grid[y + 1][x + 1] if x < w - 1 else 0

            if cell:
                cell = 1 if count >= 2 and count <=3 else 0
            else:
                cell = 1 if count == 3 else 0
                
            # print(y, x, cell)
            
            temp[y][x] = cell
            
    return temp

def create_grid(w, h, alive=0.5, filename=None, overwrite=False):
    '''Function that creats large grids based on the given dimentions and percentage of alive cells.
    Code from https://github.com/girgink/game-of-life/blob/main/game.py'''
    
    if alive < 0 or alive > 1.0:
        raise ValueError("Invalid alive percentage.")
        # raise ValueError - user defined ValueError unlike 'except'
    
    if not filename:
        filename = f"input_{w}x{h}_{alive}.txt"

    if os.path.exists(filename) and not overwrite:
        raise FileExistsError
        
    m = round(w * h * alive)
    # no of cells that are to be filled . Round?
    
    skip = {}

    with open(filename, "w") as f:
        f.write(f"{w} {h}\n")    #dims
        while m > 0:
            # keep filling up m number of cells and count down to zero
            x, y = random.randrange(w), random.randrange(h)
            # random range to fill
            
            # I thought, if grid[x][y] is not filled then fill it
            # directly grid can be constructed & save file simultaneously
                        
            idx = y * w + x
            # multiply row with total width and add column number 
            # to get unique id for each cell
                        
            if idx not in skip:
                f.write(f"{y} {x}\n")
                skip[idx] = True
                # key idx, value true
                m -= 1

def save_grid_as_rle(grid, filename, overwrite=False):
    '''Function converts input grid into interoperable open source Golly format.
    The .rle format - run length encoded format is is commonly-used for storing patterns.
    Code from https://github.com/girgink/game-of-life/blob/main/game.py'''
    
    if os.path.exists(filename) and not overwrite:
        raise FileExistsError

    w, h = grid_dim(grid)

    with open(filename, "w") as f:
        f.write(f"x = {w}, y = {h}, rule = B3/S23:P{w},{h}\n")
        str = ""
        val = None
        run = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if val is None:
                    val = cell
                    run = 1
                elif val == cell:
                    run += 1
                else:
                    str += "{}{}".format(run if run > 1 else "", "o" if val == 1 else "b")
                    if len(str) > 68:
                        f.write(f"{str}\n")
                        str = ""
                    val = cell
                    run = 1
            if val is not None:
                str += "{}{}".format(run if run > 1 else "", "o" if val == 1 else "b")
                val = None
            str += "$"
            if len(str) > 68:
                f.write(f"{str}\n")
                str = ""

        f.write(f"{str}!\n")


def main():
    # print(sys.argv) # gives a list of arg that are given as arguments with game.py
    
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
    print (grid)
    
    w, h = grid_dim(grid)
    # print("The grid has {} rows and {} columns.".format(h, w))
    
    start = time.time()    # calcualates time for processing grid generations
    
    for i in range(n):
        grid = tick(grid)
        print("{} generation GRID:\n{}".format(i+1,grid))
    
    print("{} seconds elapsed for {} generations.".format(round(time.time() - start, 7), n))
    
    save_grid(grid, output_name)
    

if __name__ == "__main__":
    main()