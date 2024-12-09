import sys
matchingPatterns = (
    ("M.S", ".A.", "M.S"),
    ("M.M", ".A.", "S.S"),
    ("S.S", ".A.", "M.M"),
    ("S.M", ".A.", "S.M")
)

matchingPatterns2 = (
    ("MSAMS"),
    ("MMASS"),
    ("SSAMM"),
    ("SMASM")
)

def checkMatch2(text, colNum, rowNum):
    swatch = text[colNum][rowNum] + text[colNum][rowNum + 2] + text[colNum+1][rowNum+1] + text[colNum+2][rowNum] + text[colNum+2][rowNum+2]
    return swatch in matchingPatterns2

def checkMatch(text, colNum, rowNum):
    for pattern in matchingPatterns:
        match = True
        if colNum + 3 >= len(text) or rowNum + 3 >= len(text[0]):
            continue
        for i in range(3):
            for j in range(3):
                if pattern[i][j] == "." or pattern[i][j] == text[colNum + i][rowNum + j]:
                    pass
                else:
                    match = False
        if(match):
            return True
    return False

                    

def main(filename):
    with open(filename, 'r') as inputfile:
        text = [line.strip() for line in inputfile]
    sum = 0
    for rowNum in range(len(text) - 2):
        for colNum in range(len(text[0]) - 2):
            if(checkMatch2(text, rowNum, colNum)):
                sum += 1
    print(sum)


# main("day04/input")
if __name__ == "__main__":
    main(sys.argv[1])


# 1816 is too low