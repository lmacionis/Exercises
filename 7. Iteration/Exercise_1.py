"""
Write a function to count how many odd numbers are in a list.
"""
# Also try this with the while loop, not only for, I think it should be possible.

list = [1, 2, 3, 4, 5, 13, 16, 27, 26, 1111111111]
odd_count = 0

"""                     Verion from youtube:
def is_odd(number):
    return number % 2 != 0


def count_odd_num(numbers):
    odd_count = 0

    for number in numbers:
        if is_odd(number):
            odd_count += 1
    return odd_count


print(count_odd_num(list))
"""


# Everything in one  function, remade it by me.
def count_odd_num(numbers):

    odd_count = 0

    for i in numbers:
        if i % 2 != 0:
            odd_count += 1
    return odd_count


print(count_odd_num(list))