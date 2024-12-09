import sys

def isSafe(report):
    differences = [report[i] - report[i + 1] for i in range(len(report) - 1)]
    numSafe = 0
    isIncreasing = differences[0] > 0
    for difference in differences:
        if isIncreasing:
            num = difference
        else:
            num = -difference
        if not (1 <= num <= 3):
            return False
    return True

def removeLevels(report):
    if(isSafe(report)):
        return True
    for i in range(len(report)):
        withoutLevel = report[:]
        withoutLevel.pop(i)
        if isSafe(withoutLevel):
            return True
    return False

def main(filename):
    with open(filename, 'r') as inputfile:
        reports = [[int(val) for val in line.split()] for line in inputfile]
    # print(reports)

    sum = 0
    for report in reports:
        print(report, end=" ")
        if(removeLevels(report)):
            sum += 1
            print("safe")
    print(sum)            


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        main(sys.argv[1])
    else:
        main("day02/testinput")