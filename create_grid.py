import sys
from game import create_grid

# code from https://github.com/girgink/game-of-life/blob/main/create_grid.py

def main():

    num_args = len(sys.argv)

    try:
        w, h = int(sys.argv[1]), int(sys.argv[2])
    except IndexError:
        exit("Invalid number of arguments.")

    if w <= 0:
        raise ValueError("Invalid grid width.")

    if h <= 0:
        raise ValueError("Invalid grid height.")

    opts = {}

    if num_args > 3:
        # didn't fully understand > 3 shouldn't it be > 2
        opts["alive"] = float(sys.argv[3])
        # default alive is set to 0.5 in the method

    if num_args > 4:
        opts["filename"] = sys.argv[5]

    if num_args > 5:
        val = str(sys.argv[6]).upper()
        opts["overwrite"] = val in ["YES", "Y", "1", "TRUE"]
        # converts UPPER then checks if in list saves as True or False

    create_grid(w, h, **opts)
    # **opts unpacks dict just created


if __name__ == "__main__":
    main()