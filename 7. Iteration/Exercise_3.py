"""
Sum up all the negative numbers in a list.
"""

list = [-1, -2, -3, 4, 5, 1, 6, -1, -8]

def sum_negative_num(numbers):
    negative_num = 0
    for i in numbers:
        if i < 0:
            negative_num = negative_num + i
    return negative_num


print(sum_negative_num(list))