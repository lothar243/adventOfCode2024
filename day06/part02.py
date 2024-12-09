import sys, copy

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

guardCharacters = ("^", ">", "v", "<")
directions = (up, right, down, left)


def findGuard(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            currentChar = next(iter(map[i][j]))
            if currentChar in guardCharacters:
                return i, j, guardCharacters.index(currentChar)

def printMap(map):
    for row in map:
        for chars in row:
            horizontalMove = "<" in chars or ">" in chars
            verticalMove = "v" in chars or "^" in chars
            if horizontalMove and verticalMove:
                print("+", end="")
            elif horizontalMove:
                print("-", end="")
            elif verticalMove:
                print("|", end="")
            else:
                print(next(iter(chars)), end="")
                
        print()

def onMap(map, y, x):
    return 0 <= y < len(map) and 0 <= x < len(map[0])

def move(map, y, x, directionIndex):
    # map[y][x] = "X"
    nextPosY = y + directions[directionIndex][0]
    nextPosX = x + directions[directionIndex][1]
    if(onMap(map, nextPosY, nextPosY)):
        if(guardCharacters[directionIndex] in map[nextPosY][nextPosY]):
                return 0,0,0,True
    if(not onMap(map, nextPosY, nextPosX) or "#" not in map[nextPosY][nextPosX]):
        # move forward
        y = nextPosY
        x = nextPosX
        if(onMap(map, y, x)):
            map[y][x].add(guardCharacters[directionIndex])
    else:
        # turn
        directionIndex = (directionIndex + 1) % 4
        if(onMap(map, y, x)):
            map[y][x].add(guardCharacters[directionIndex])
    return y, x, directionIndex, False

def hasLoop(map, guardY, guardX, guardDirectionIndex):

    while(onMap(map, guardY, guardX)):
        guardY, guardX, guardDirectionIndex, loopDetected = move(map, guardY, guardX, guardDirectionIndex)
        printMap(map)
        # input()
        if(loopDetected):
            return True
    return False

def main(filename):
    with open(filename, 'r') as inputfile:
        map = [[set(char) for char in line.strip()] for line in inputfile]
    # print(map)
    # printMap(map)
    # print(findGuard(map))
    guardY, guardX, guardDirectionIndex = findGuard(map)
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            testMap = copy.deepcopy(map)
            if testMap[i][j] == set("."):
                testMap[i][j] = set("#")
                if(hasLoop(testMap, guardY, guardX, guardDirectionIndex)):
                    printMap(testMap)
                    sum += 1
    print(sum)

main("day06/example")
if __name__ == "__main__":
    main(sys.argv[1])