import sys

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

guardCharacters = ("^", ">", "v", "<")
directions = (up, right, down, left)


def findGuard(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in guardCharacters:
                return i, j, guardCharacters.index(map[i][j])

def printMap(map):
    for row in map:
        for char in row:
            print(char, end="")
        print()

def onMap(map, y, x):
    return 0 <= y < len(map) and 0 <= x < len(map[0])

def move(map, y, x, directionIndex):
    map[y][x] = "X"
    nextPosY = y + directions[directionIndex][0]
    nextPosX = x + directions[directionIndex][1]
    if(not onMap(map, nextPosY, nextPosX) or map[nextPosY][nextPosX] != "#"):
        # move forward
        y = nextPosY
        x = nextPosX
        if(onMap(map, y, x)):
            map[y][x] = guardCharacters[directionIndex]
    else:
        # turn
        directionIndex = (directionIndex + 1) % 4
    if(onMap(map, y, x)):
        map[y][x] = guardCharacters[directionIndex]
    return y, x, directionIndex

def countLocations(map):
    sum = 0
    for row in map:
        for char in row:
            if(char == "X"):
                sum += 1
    return sum

def main(filename):
    with open(filename, 'r') as inputfile:
        map = [[char for char in line.strip()] for line in inputfile]
    # print(map)
    # printMap(map)
    # print(findGuard(map))
    guardY, guardX, guardDirectionIndex = findGuard(map)
    while(onMap(map, guardY, guardX)):
        guardY, guardX, guardDirectionIndex = move(map, guardY, guardX, guardDirectionIndex)
        # printMap(map)
        # input()
    print(countLocations(map))
    

if __name__ == "__main__":
    main(sys.argv[1])