Mini-Project 1: Search

In this mini-project, your task is to implement general-purpose search algorithms and use them in solving maze problems. More concretely, you will program an agent to find a path through the maze and reach the exit.

Your program should run using Python 3.7. Your code can only import extra modules, but only if they are part of the standard python library.

Your program will solve the problem of finding the shortest path given an initial start state and one goal state. The maze layout will be provided as a simple text file, in which '%' means obstacles, 'P' is the starting position, and '.' represents the goal . See the sample mazes files for an illustration.

Maze1.txtPreview the document

Maze2.txtPreview the document

Maze3.txtPreview the document


The agent can move in one of four directions North, West, South, East.

You should implement the state representation, transition model, and goal test necessary to solve the problem. Then
implement the following search algorithms that were covered in class and are in the textbook:

-Depth-first search
-Breadth-first search
-Greedy best-first search
-A* search

For this part of the assignment, you will use the Manhattan distance from the current position to the goal as the heuristic function for greedy and A* search.

For each maze, your report should include a solution output (this can be shown in the command line), the solution cost, and the number of nodes expanded in your search.

You will submit this mini-project through canvas. You will upload only two files:

-search.py - the python file with your solution
-report.pdf - a project report on your implementation

Your program should run as follows:

python3 search.py --method astar maze.txt

Where astar is the name of the method, which can be one of depth, breadth, greedy, or astar, and maze.txt is the input file. We will
supply three mazes as shown above that you can use to test your program, but we will test other mazes.

You should include in your report the name of the team members (you can work in pairs). Please
describe the algorithms and data structures used that you used for the implementation of
all four search strategies. Answer the following questions on your report: what is a state? What is a node? Are they the same or different in your implementations? What is the frontier? Do you maintain an explored states list? How are repeated states detected and managed?