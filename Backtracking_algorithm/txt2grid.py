"""
Fiiename:txt2grid.py
Turn a .txt to a Grid
"""
from Backtracking_algorithm.Grid import Grid

class txtGrid(Grid):

    def __init__(self,rows,columns,attribute=None):
        Grid.__init__(self,rows,columns,fillValue=None)

    def show(self):
        string = ''
        for row in self._data:
            for column in row:
                string=string+column
            string=string+'\n'
        print(string)

def txt2grid(filename):

    with open(filename,'r') as f1:
        lines=f1.readlines()

    grid=txtGrid(len(lines),len(lines[0])-1)

    for row_index in range(len(lines)):
        row=lines[row_index].rstrip('\n')
        for column_index in range(len(row)):
            index=[row_index,column_index]
            grid[index]=lines[row_index][column_index]

    return grid


if __name__=='__main__':
    a=txt2grid('/Users/jiangmingda/Desktop/test.txt')
    a.show()