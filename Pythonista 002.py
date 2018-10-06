"""
Author : RyuCoder
Website: http://ryucoder.in/
Purpose : Algorithm to print if a sentence is a palindrome or not without reversing it
Problems with the code: None
Notes: Sentence is case sensitive in nature
"""

import math

def is_palindrome(sentence):

    table = []
    length = len(sentence)

    for index in range(math.ceil(length/2)):
        if sentence[index] == sentence[(length-1)-index]:  # length-1 because of zero based index
            table.append(True)
        else:
            table.append(False)

    return all(table)


def main():

    result = is_palindrome("MmmM")
    print(result)

    
if __name__ == "__main__":
    main()
