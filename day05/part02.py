import sys

orderingRules = {}

def isInOrder(manual):
    restrictedPages = set()
    for page in reversed(manual):
        if page in restrictedPages:
            return False
        restrictedPages.update(orderingRules.get(page, set()))
    return True

def reorderManual(manual):
    for i, page in enumerate(manual):
        for j in range(i + 1, len(manual)):
            print(f"Checking: {manual[i]} and {manual[j]}")
            if manual[i] in orderingRules.get(manual[j], set()):
                print(f"swapping pages {manual[i]} and {manual[j]}")
                temp = manual[i]
                manual[i] = manual[j]
                manual[j] = temp

def middlePage(manual):
    return manual[(len(manual) - 1) // 2]

def main(filename):
    with open(filename, 'r') as inputfile:
        for line in inputfile:
            if(line == "\n"):
                break
            first, second = line.split("|")
            first = int(first)
            second = int(second)
            rule = orderingRules.get(first, set())
            rule.add(second)
            orderingRules[first] = rule
        manuals = [[int(value) for value in line.strip().split(",")] for line in inputfile]
    print(orderingRules)
    print(manuals)

    # reading the manual backward will give me a set of restricted pages
    
    sum = 0
    for manual in manuals:
        # print(manual)
        # print(isInOrder(manual))
        # print(middlePage(manual))
        if(not isInOrder(manual)):
            print("not in order")
            count = 0
            while(not isInOrder(manual) and count < 10):
                print(manual)
                reorderManual(manual)
                count += 1
            print(manual)
            sum += middlePage(manual)
    print(sum)
    

# main("day05/example")
if __name__ == "__main__":
    main(sys.argv[1])