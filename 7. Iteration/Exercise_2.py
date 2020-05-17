"""
Sum up all the even numbers in a list.
"""

list = [1, 2, 3, 4, 5, 6, 7, 8, 8]

def even_num(n):
    even_num_sum = 0
    for i in n:
        if i % 2 == 0 :
            even_num_sum = even_num_sum + i
    return even_num_sum


print(even_num(list))


# Done by the book

