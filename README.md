# Game of Life
This is an implementation of Conway's Game of Life in Python. The project is carried out mainly to understand how optimising python script can effect processing of big data. With each version of the code, the program is able to handle biger sizes of Game of Life grid in a more efficient manner. 

## Description

From [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. 

At each step in time, the following transitions occur:

* Any **live** cell with *fewer than two live neighbours* **dies**, as if by underpopulation.
* Any **live** cell with *two or three live neighbours* **lives** on to the next generation.
* Any **live** cell with *more than three live neighbours* **dies**, as if by overpopulation.
* Any **dead** cell with *exactly three live neighbours* becomes a **live** cell, as if by reproduction.

These <a name="rules"> <span style="color:blue"> rules </span> </a> can be condensed into the following:

1. Any **live** cell with *two or three live neighbours* **survives**.
2. Any **dead** cell with *three live neighbours* becomes a **live** cell.
3. All other **live** cells **die** in the next generation. Similarly, all other **dead** cells stay **dead**.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules **simultaneously** to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a **tick**. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

## Implementation

* Input text file name, output text file name, and number of generations are provided as arguments to the script.
* The script reads the size of the grid from the first line of the input text file. The initial pattern is read from the remaining lines.
* It then applies the [rules](#rules) for the number of generations indicated.
* It writes the final pattern to the output file.

## Input and output file format
* Input and output files are of text format.
* The first line indicates the width and height of the grid as unsigned integer values separated by a space.
* The remaining lines indicate the initial location of the living cells. Each line has two unsigned integer values separated by space indicating vertical(row) and horizontal(column) coordinates of the living cells, respectively.
    * The top left cell has the coordinates of (0, 0)
    * Valid vertical coordinate values range between \[0 - height), increasing from top to bottom.
    * Valid horizontal coordinate values range between \[1 - width), increasing from left to right.

## Example

```
python game.py input.txt output.txt 3
```

Input:
```
3 5
0 3
0 0
1 2
1 4
2 1
```
[input.txt](./input.txt)

Output:
```
3 5
0 2
0 3
1 2
1 3
2 2
2 3
```
[output.txt](./output.txt)

<!---write a lot about reproducibility--->

## Create large grids
To create large grids with randomly assigned fill percentage, the create_grid() function can be used. This can be called as the following example
```
# python ./create_grid.py *unsigned_int_width* *unsigned_int_height* *unsigned_float_alivePercentage_Between0-1* *Optional_output_filename*

python ./create_grid.py 100 100 0.5 
```

## Convert formats
To convert .txt grid to interoperable open source .rle format, the convert_to_rle() fucntion can be used as follows
```
python convert_to_rle.py input_filename.txt
```

