"""
Write a function sum_of_squares(xs) that computes the sum of the squares of the
numbers in the list xs. For example, sum_of_squares([2, 3, 4])
should return 4+9+16 which is 29:

test(sum_of_squares([2, 3, 4]) == 29)
test(sum_of_squares([ ]) == 0)
test(sum_of_squares([2, -3, 4]) == 29)
"""

xs = []

def sum_of_squares(xs):
    square_num = 0
    sum = 0
    for i in xs:
        square_num = i**2
        sum += square_num
    return sum


print(sum_of_squares([2, 3, 4]))