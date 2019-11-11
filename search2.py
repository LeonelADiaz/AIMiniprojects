import argparse
from queue import PriorityQueue

start = None
end = None


def main(arguments):
    global start
    global end
    maze = arguments.mazeName
    maze = readMaze(maze)
    searchType = arguments.search
    createNodes(maze)

    if searchType == 'astar':
        expanded = astar(maze, start)
    elif searchType == 'dfs':
        expanded = dfs(maze, start)
    elif searchType == 'greedy':
        expanded = greedy(maze, start)
    else:
        expanded = bfs(maze, start)

    path = Path(maze, end)
    printMaze(maze)
    print("Path Cost: " + str(path))
    print("Expanded Nodes: " + str(expanded))


def addChild(nodeA, nodeB):
    nodeA.children.append(nodeB)
    nodeB.children.append(nodeA)


# Reads given maze file
def readMaze(mazeFile):
    maze = list()
    # open mazeFile in read mode, close it after
    with open(mazeFile) as file:
        # add each line character by character into maze list
        for line in file:
            maze.append(list(line.rstrip()))
    return maze


# Creates the nodes
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


# changes the value of node
# used to show path
def testNode(maze, node):
    if maze[node.position[0]][node.position[1]] == " ":
        maze[node.position[0]][node.position[1]] = "+"
    elif maze[node.position[0]][node.position[1]] == ".":
        maze[node.position[0]][node.position[1]] = "E"
    elif maze[node.position[0]][node.position[1]] == "P":
        maze[node.position[0]][node.position[1]] = "S"


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


# returns manhattan distance of a node
def manhattan(nodeA):
    x1 = nodeA.position[0]
    y1 = nodeA.position[1]
    x2 = end.position[0]
    y2 = end.position[1]

    distance = abs(x1-x2) + abs(y1-y2)
    return distance


# uses greedy algorithm to navigate maze where each node has
# a heuristic = manhattandistance(to end)
def greedy(maze, node):
    count = 0
    nodesExpanded = 0

    queue = PriorityQueue()
    queue.put((manhattan(node), nodesExpanded, node))
    visited = set()

    while queue:
        node = queue.get()
        node = node[2]
        visited.add(node)
        count += 1
        if maze[node.position[0]][node.position[1]] == "." or \
                maze[node.position[0]][node.position[1]] == "E":
            break
        if node in visited:

            for child in range(len(node.children)):
                if node.children[child] not in visited and node.children[child].parent is None:
                    nodesExpanded = nodesExpanded + 1
                    child = node.children[child]
                    child.parent = node
                    queue.put((manhattan(child), nodesExpanded, child))
    return count


# uses astar algorithm to navigate maze where each node has
# a heuristic = pathcost + manhattandistance(to end)
def astar(maze, node):
    count = 0
    nodesExpanded = 0

    queue = PriorityQueue()
    queue.put((manhattan(node), nodesExpanded, node))
    visited = set()

    while queue:
        node = queue.get()
        node = node[2]
        visited.add(node)
        count += 1
        if maze[node.position[0]][node.position[1]] == "." or \
                maze[node.position[0]][node.position[1]] == "E":
            break
        if node in visited:

            for child in range(len(node.children)):
                if node.children[child] not in visited and node.children[child].parent is None:
                    nodesExpanded = nodesExpanded + 1
                    child = node.children[child]
                    child.parent = node
                    queue.put(((manhattan(child) + nodesExpanded), nodesExpanded, child))
    return count


# returns path cost by starting at 'node'
# and going through each parent until reaching the root
def Path(maze, node):
    count = 0
    while node.parent is not None:
        testNode(maze, node)
        node = node.parent
        count += 1
    return count


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


class Node(object):
    def __init__(self, position):
        self.position = position
        self.parent = None
        self.children = []


# Setup for command line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Implements various search through a given maze')
    parser.add_argument('--method', dest="search", type=str, default="bfs",
                        choices=["bfs", "dfs", "greedy", "astar"],
                        help='search method - default bfs')
    parser.add_argument('mazeName', help='Maze file Name')
    args = parser.parse_args()
    main(args)
