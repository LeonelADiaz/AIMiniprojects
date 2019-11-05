#Start search Solution here
import argparse

#Reading line arguments
parser = argparse.ArgumentParser(description='Implements various search through a given maze')
parser.add_argument('--method', help='If you wish to supply a search to use or not')
parser.add_argument('mazeFile', help='Maze file Name')
args = parser.parse_args()

#Assigns a default search to use if one is not provided
search = "depth"
if args.method:
    search = args.method

#Find the shortest path given an initial start state and one goal state.
#Start state is P & Goal state is .

#Move in one of four directions (One function)

#Need State representation, transition model, and goal test.

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

def dfs():
    print ("Depth first search")

def bfs():
    print ("Breadth first search")

def greedy():
    print ("Greedy Search")

def astar():
    print("Astar* Search")

def main():
    desiredSearch(search)

if __name__ == "__main__":
    main()





