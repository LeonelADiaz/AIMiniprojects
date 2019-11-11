"""TODO:Need State representation, transition model, and goal test.
        Find the shortest path given an initial start state and one goal state.
        Start state is P & Goal state is .

        Pretty much implement the missing code in Problem and GridProblem,
        as well as implementing greedy and A*. Everything else should be good.
        Uncomment main() when ready to test.
"""

#Start search Solution here with imports
import argparse
import bisect
import math
import random
import sys
from collections import deque
from queue import PriorityQueue

#Reading line arguments
parser = argparse.ArgumentParser(description='Implements various search through a given maze')
parser.add_argument('--method', help='If you wish to supply a search to use or not')
parser.add_argument('mazeFile', help='Maze file Name')
args = parser.parse_args()

#Assigns a default search to use if one is not provided
search = "depth"
if args.method:
    search = args.method

global start
global end

#Node class
class Node(object):
    def __init__(self, position):
        self.position = position
        self.parent = None
        self.children = []

def Path(maze, node):
    count = 0
    while node.parent is not None:
        testNode(maze, node)
        node = node.parent
        count += 1
    return count

def testNode(maze, node):
    if maze[node.position[0]][node.position[1]] == " ":
        maze[node.position[0]][node.position[1]] = "+"
    elif maze[node.position[0]][node.position[1]] == ".":
        maze[node.position[0]][node.position[1]] = "E"
    elif maze[node.position[0]][node.position[1]] == "P":
        maze[node.position[0]][node.position[1]] = "S"

def addChild(nodeA, nodeB):
    nodeA.children.append(nodeB)
    nodeB.children.append(nodeA)

def readMaze(mazeFile):
    maze = list()
    with open(mazeFile) as file:
        for line in file:
            maze.append(list(line.rstrip()))
    return maze

def createNodes(maze):
    prevNode = Node(-1)
    currentNode = Node(-1)
    topNode = [Node(-1)]*len(maze[0])
    for i in range(len(maze)):
        prevNode = Node(-1)
        for j in range(len(maze[0])):
            if maze[i][j] == "%":
                prevNode = Node(-1)
                topNode[j] = Node(-1)
            else:
                currentNode = Node((i, j))
            if prevNode.position is not -1:
                addChild(currentNode, prevNode)
                prevNode = currentNode
            if topNode[j].position is not -1:
                addChild(currentNode, topNode[j])
                topNode[j] = currentNode
            if maze[currentNode.position[0]][currentNode.position[1]] == "P":
                global start
                start = currentNode
                testNode(maze, start)
            if maze[currentNode.position[0]][currentNode.position[1]] == "."\
            or maze[currentNode.position[0]][currentNode.position[1]] == "E":
                global end
                end = currentNode

def readMaze(mazeFile):
    maze = list()
    # open mazeFile in read mode, close it after
    with open(mazeFile) as file:
        # add each line character by character into maze list
        for line in file:
            maze.append(list(line.rstrip()))
    return maze

# Prints given maze file
def printMaze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(maze[i][j], end="")
        print()


# Returns the starting position of the maze
# start position denoted as "P"
def findStart(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "P":
                return tuple([i, j])
    return None


# Returns the end position of the maze
# end position denoted as "."
def findEnd(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == ".":
                return tuple([i, j])
    return None


#TODO: Actual search algorithm definition
#Cases for different search algorithms, abd runs the selected algorithm
def desiredSearch(x):
    if(search == "breadth"):
        bfs()
    elif(search == "greedy"):
        greedy()
    elif(search == "astar"):
        astar()
    else:
        dfs()

# uses breadth first search algorithm to navigate maze
# with a queue
def bfs(maze, node):
    count = 0
    queue = [node]

    visited = set()

    while queue:
        node = queue.pop(0)
        visited.add(node)
        count += 1

        if maze[node.position[0]][node.position[1]] == "." or \
                maze[node.position[0]][node.position[1]] == "E":
            break
        else:

            for child in range(len(node.children)):
                if node.children[child] not in visited and node.children[child].parent is None:
                    node.children[child].parent = node
                    queue.append(node.children[child])

    return count


# uses depth first search algorithm to navigate maze
# with a stack
def dfs(maze, node):
    count = 0

    stack = [node]
    visited = set()

    while stack:
        node = stack.pop()
        visited.add(node)
        count += 1

        if maze[node.position[0]][node.position[1]] == "." or \
                maze[node.position[0]][node.position[1]] == "E":
            break
        if node in visited:

            for child in range(len(node.children)):
                if node.children[child] not in visited and node.children[child].parent is None:
                    node.children[child].parent = node
                    stack.append(node.children[child])
    return count

maze = args.mazeFile
maze = readMaze(maze)


path = Node.Path(maze, end)
printMaze(maze)
print("Path Cost: " + str(path))

#TODO: Greedy and Astar*
def greedy():
    print ("Greedy Search")

def astar():
    print("Astar* Search")

def main():
    desiredSearch(search)
    
if __name__ == "__main__":
    main()





