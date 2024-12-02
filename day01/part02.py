import sys

def main(filename):
    with open(filename, 'r') as inputfile:
        list1 = []
        valueToCount = {}
        for line in inputfile:
            val1, val2 = line.split()
            val1 = int(val1)
            val2 = int(val2)
            list1.append(val1)
            valueToCount[val2] = valueToCount.get(val2, 0) + 1
    sum = 0
    for value in list1:
        sum += value * valueToCount.get(value, 0)

    print(sum)


if __name__ == "__main__":
    main(sys.argv[1])