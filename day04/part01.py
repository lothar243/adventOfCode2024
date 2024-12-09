import sys

directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
targetWord = "XMAS"

def followWord(currentPos, direction, targetIndex, wordGrid):
    # assume the current letter matches and check for the next
    
    # start by checking if we're done
    if(targetIndex == 3):
        return True
    nextY, nextX = (currentPos[0] + direction[0], currentPos[1] + direction[1])
    nextIndex = targetIndex + 1
    if not (0 <= nextY < len(wordGrid) and 0 <= nextX < len(wordGrid[0]) and wordGrid[nextY][nextX] == targetWord[nextIndex]):
        return False
    return followWord((nextY, nextX), direction, nextIndex, wordGrid)

def main(filename):
    with open(filename, 'r') as inputfile:
        text = [line.strip() for line in inputfile]
    sum = 0
    for rowNum in range(len(text)):
        for colNum in range(len(text[0])):
            if(text[rowNum][colNum] == "X"):
                for i in range(8):
                    if(followWord((rowNum, colNum), directions[i], 0, text)):
                        sum += 1
    print(sum)



if __name__ == "__main__":
    main(sys.argv[1])