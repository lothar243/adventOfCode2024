import sys, re

def main(filename):
    with open(filename, 'r') as inputfile:
        text = inputfile.read()
    matches = re.findall(r"mul\(\d+,\d+\)", text)
    # print(matches)
    sum = 0
    for match in matches:
        num1, num2 = re.findall(r"\d+", match)
        sum += int(num1) * int(num2)
    print(sum)


if __name__ == "__main__":
    main(sys.argv[1])