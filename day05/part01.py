import sys

orderingRules = {}

def isInOrder(manual):
    restrictedPages = set()
    for page in reversed(manual):
        if page in restrictedPages:
            return False
        restrictedPages.update(orderingRules.get(page, set()))
    return True

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
        if(isInOrder(manual)):
            sum += middlePage(manual)
    print(sum)
    

if __name__ == "__main__":
    main(sys.argv[1])