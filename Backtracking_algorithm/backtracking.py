"""
Filename:backtracking.py
startingpoint:'P'
endingpoint:'T'
path can be went through:' '
wall can't be went through:'*'
If finding the path,shows it and returns 'One path has been found'
Otherwise,returns 'Can't find a path'
"""
from Backtracking_algorithm.txt2grid import txt2grid
from Stack.LinkedStack import LinkedStack



def finding(grid):
    """Find the position of the starting-point and the ending-point"""
    height=grid.getHeight()
    weight=grid.getWidth()
    for i in range(height):
        for j in range(weight):
            index=[i,j]
            if grid[index]=='P':
                starting_index=index
                return starting_index
            else:continue
    return KeyError('Can\'t find \'P\'')

def findway(point_index,stack,grid):
    """find way in the order of up、down、left and right"""
    if grid[point_index]=='P':
        pass
    else:
        grid[point_index]='-'

    point_x=point_index[0]
    point_y=point_index[1]

    if grid[point_x,point_y+1]==' ':
        stack.push([point_x,point_y+1])
    if grid[point_x,point_y-1]==' ':
        stack.push([point_x,point_y-1])
    if grid[point_x+1, point_y] == ' ':
        stack.push([point_x+1, point_y])
    if grid[point_x-1,point_y]==' ':
        stack.push([point_x-1,point_y])
    if grid[point_x,point_y+1]=='T' or grid[point_x,point_y-1]=='T' \
            or grid[point_x+1, point_y] == 'T' or grid[point_x-1,point_y]=='T':
        return True

def main(grid):
    start_index=finding(grid)
    stack=LinkedStack()
    stack.push(start_index)
    while not stack.isEmpty():
        if findway(stack.pop(),stack,grid):
            return True
    return False


if __name__=='__main__':
    filename = 'Backtracking_algorithm/test.txt'
    grid = txt2grid(filename)
    if main(grid):
        print('Find a path')
    else:
        print('Can\'t find a path')
    grid.show()

