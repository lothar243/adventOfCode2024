import sys

def main(filename):
    with open(filename, 'r') as inputfile:
        reports = [[int(val) for val in line.split()] for line in inputfile]
    # print(reports)

    differences = [ [report[i] - report[i + 1] for i in range(len(report) - 1)] for report in reports]
    # print(differences)
    numSafe = 0
    for difference in differences:
        isIncreasing = difference[0] > 0
        for i in range(len(difference) - 1):
            


if __name__ == "__main__":
    main(sys.argv[1])