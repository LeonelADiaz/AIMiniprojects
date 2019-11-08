#Reads a file, stores the maze, and puts out a list of coordinates for the barriers
result = []

with open("Maze3.txt") as fileobj:
    for line in fileobj:
        result.append(line) 
 
newResult = [x[:-1] for x in result]
newResult[len(newResult) - 1] = newResult[len(newResult) - 1] + "%"

i = 0
j = 0

barriers = []

for row in newResult:
    for col in row:
        if(col == "%"):
            barriers.append((i, j))
        j = j + 1
    i = i + 1
    j = 0

print (barriers)
print (len(newResult[0]))