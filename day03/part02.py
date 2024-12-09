import sys, re

def multiplyAndSum(text):
    matches = re.findall(r"mul\(\d+,\d+\)", text)
    # print(matches)
    sum = 0
    for match in matches:
        num1, num2 = re.findall(r"\d+", match)
        sum += int(num1) * int(num2)
    return sum

def removeDont(text):
    text = re.sub(r"don't\(\).*?do\(\)", "", text)
    text = re.sub(r"don't\(\).*?$", "", text)
    print(text)
    return text

def main(filename):
    with open(filename, 'r') as inputfile:
        text = inputfile.read()
    print(multiplyAndSum(removeDont(text)))

if __name__ == "__main__":
    main(sys.argv[1])

