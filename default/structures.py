#!env/bin/python

import sys

class Lattice:
    """A simple lattice structure"""
    pos = {}
    grid = []

    def __init__(self):
        self.init_grid(1,1)

    def __init__(self,r,c):
        self.init_grid(r,c)

    def init_grid(self,r,c):
        global grid,pos
        pos={"x" : 0, "y" : 0}
        grid = []
        for y in range(0,r,1):
            row = []
            for x in range(0,c,1):
                row.append(0)
            grid.append(row)

    def get_grid(self):
        return grid

    def get_max_x(self):
        return len(grid[0])-1

    def get_max_y(self):
        return len(grid)-1

    def print_grid(self):
        for y in grid:
            for x in y:
                sys.stdout.write(str(x)+'\t')
            sys.stdout.write('\n')
            sys.stdout.flush()

    def get_pos(self):
        result={"x" : pos["x"], "y" : pos["y"]}
        return result

    def set_pos(self,x,y):
        pos["x"] = x
        pos["y"] = y

    def set_value(self,n):
        grid[pos["y"]][pos["x"]] = n

    def get_value(self):
        return grid[pos["y"]][pos["x"]]

    def get_neighbors(self):
        result = []
        if pos["x"] > 0:
            result.append({"x" : pos["x"] - 1, "y" : pos["y"]})
        if pos["y"] > 0:
            result.append({"x" : pos["x"], "y" : pos["y"] - 1})
        if pos["x"] < self.get_max_x():
            result.append({"x" : pos["x"] + 1, "y" : pos["y"]})
        if pos["y"] < self.get_max_y():
            result.append({"x" : pos["x"], "y" : pos["y"] + 1})
        return result
