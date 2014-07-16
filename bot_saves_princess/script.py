#!env/bin/python

def displayPathtoPrincess(n,grid):
    '''
    Find the shortest path to the princess and print it
    '''

    m = {'x': 0, 'y': 0}
    p = {'x': 0, 'y': 0}

    for x in xrange(n):
    # Initialize the positions of the princess and mario
        for y in xrange(n):
            if grid[y][x] == 'p': # Store x,y backwards in the grid object
                p['x'] = x
                p['y'] = y
            elif grid[x][y] == 'm':
                m['x'] = x
                m['y'] = y

    while m != p: # As long as m isn't in the same space as p
        xdiff = m['x'] - p['x'] # Distance on the X axis
        ydiff = m['y'] - p['y'] # Distance on the Y axis

        if abs(xdiff) > abs(ydiff): # If X > Y we move along the X axis
            if xdiff > 0:
                print "LEFT"
                m['x'] -= 1
            else:
                print "RIGHT"
                m['x'] += 1
        else:
            if ydiff > 0:
                print "UP"
                m['y'] -= 1
            else:
                print "DOWN"
                m['y'] += 1
            

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)

