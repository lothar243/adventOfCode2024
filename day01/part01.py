import sys

def main(filename):
    with open(filename, 'r') as inputfile:
        list1 = []
        list2 = []
        for line in inputfile:
            val1, val2 = line.split()
            list1.append(int(val1))
            list2.append(int(val2))
    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])

    print(sum)


if __name__ == "__main__":
    main(sys.argv[1])