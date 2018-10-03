"""
Author : RyuCoder
Website: http://ryucoder.in/
Purpose : Algorithm to print a pyramind of a string character
Problems with the code: None
Notes: String for the pattern must contain a single character 
for the pyramid to look good.
"""


def getEmptyString(times):
    emptyString = ""
    for i in range(times):
        emptyString += " "
    return emptyString 


def getPattern(times, pattern="*"):
    final_pattern = pattern + " "
    for i in range(times):
        final_pattern = final_pattern + (pattern + " ")
    return final_pattern.strip()


def main():
    pattern = ""
    # levels = list(range(int(input("\nPlease enter an integer value: \n"))))
    levels = list(range(9))
    length = len(levels)
    leftSpace = int((length + ( length - 1 ))/2)

    for index, value in enumerate(levels):
        start = getEmptyString(leftSpace)
        pattern = getPattern(index, "$")
        # end = start

        leftSpace -= 1

        # print(start + pattern + end)
        print(start + pattern)


if __name__ == "__main__":
    main()
