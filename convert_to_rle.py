import sys
import os.path
from game import read_grid, save_grid_as_rle

# code from https://github.com/girgink/game-of-life/blob/main/convert_to_rle.py

#need to change read_grid method to index from 0 for running this

def main():
    num_args = len(sys.argv)

    try:
        inp = sys.argv[1]
    except IndexError:
        sys.exit("No input file.")

    try:
        out = sys.argv[2]
    except IndexError:
        out = os.path.splitext(inp)[0] + ".rle"

    opts = {}

    if num_args > 3:
        opts["overwrite"] = sys.argv[4].upper() in ["YES", "Y", "1", "TRUE"]

    grid = read_grid(inp)

    save_grid_as_rle(grid, out, **opts)


if __name__ == "__main__":
    main()