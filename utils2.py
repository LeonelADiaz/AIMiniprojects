"""
Originally Found in http://aima.cs.berkeley.edu/python/
Modify on 11/08/2019 by Leonardo Bobadilla for the FIU AI Homework
"""
import operator, math, argparse
orientations = [(1,0), (0, 1), (-1, 0), (0, -1)]

def turn_right(orientation):
    return orientations[orientations.index(orientation)-1]

def turn_left(orientation):
    return orientations[(orientations.index(orientation)+1) % len(orientations)]

# Parse arguments for a file, and return the file.
def getFile():
    parser = argparse.ArgumentParser(description='Implements MDP to a given maze')
    parser.add_argument('mazeFile', help='Maze file name')
    args = parser.parse_args()
    mazeFile = args.mazeFile
    return mazeFile

# Reads given maze file
def readMaze(mazeFile):
    maze = list()
    # open mazeFile in read mode, close it after
    with open(mazeFile) as file:
        # add each line character by character into maze list
        for line in file:
            maze.append(list(line.rstrip()))
    return maze

# Converts empty spaces to contain 'None'
def convertPercentToNone(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "%":
                maze[i][j] = None

def convertSpacesToDefault(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == " ":
                maze[i][j] = -0.04

def convertPToOne(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "P":
                maze[i][j] = +1
def convertNToNotOne(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "N":
                maze[i][j] = -1



# Finds terminals and their location
def findP(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "+1":
                return tuple([i, j])
    return None

def findN(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "-1":
                return tuple([i, j])
    return None


def update(x, **entries):
    """Update a dict; or an object with slots; according to entries.
    >>> update({'a': 1}, a=10, b=20)
    {'a': 10, 'b': 20}
    >>> update(Struct(a=1), a=10, b=20)
    Struct(a=10, b=20)
    """
    if isinstance(x, dict):
        x.update(entries)   
    else:
        x.__dict__.update(entries) 
    return x 

def vector_add(a, b):
    """Component-wise addition of two vectors.
    >>> vector_add((0, 1), (8, 9))
    (8, 10)
    """
    return tuple(map(operator.add, a, b))


def if_(test, result, alternative):
    """Like C++ and Java's (test ? result : alternative), except
    both result and alternative are always evaluated. However, if
    either evaluates to a function, it is applied to the empty arglist,
    so you can delay execution by putting it in a lambda.
    >>> if_(2 + 2 == 4, 'ok', lambda: expensive_computation())
    'ok'
    """
    if test:
        if callable(result): return result()
        return result
    else:
        if callable(alternative): return alternative()
        return alternative

def argmin(seq, fn):
    """Return an element with lowest fn(seq[i]) score; tie goes to first one.
    >>> argmin(['one', 'to', 'three'], len)
    'to'
    """
    best = seq[0]; best_score = fn(best)
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score
    return best


def argmax(seq, fn):
    """Return an element with highest fn(seq[i]) score; tie goes to first one.
    >>> argmax(['one', 'to', 'three'], len)
    'three'
    """
    return argmin(seq, lambda x: -fn(x))

