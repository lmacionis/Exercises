"""
Now rewrite the count_letters function so that instead of traversing the string,
it repeatedly calls the find method, with the optional third parameter to
locate new occurrences of the letter being counted.
"""

# Answer is from: https://sites.google.com/site/usfcaixcacerescs110/homework-06
def count_letters(str, ch, start):
    index = start
    while index < len(str):
        if str[index] == ch:
            print(index)
        index += 1
    return -1


count_letters("banana", "a", 0)