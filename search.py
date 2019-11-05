#Start search Solution here
import argparse

#Reading line arguments

if _name_ == "_main_":
    parser = argparse.ArgumentParser(description='Implements various search through a given maze')
    parser.add_argument('mazeName', help='Maze file Name')
    # parser.add_argument('searchType', help='Which search to use')
    args = parser.parse_args()
    main(args)
#Find the shortest path given an initial start state and one goal state.
#Start state is P & Goal state is .

#Move in one of four directions (One function)

#Need State representation, transition model, and goal test.

