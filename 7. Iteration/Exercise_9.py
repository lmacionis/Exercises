"""
Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
A call to print_triangular_numbers(5) would produce the following output:

1       1
2       3
3       6
4       10
5       15

(hint: use a web search to find out what a triangular number is.)
"""

"""     Answer from the google
def print_triangular_numbers(n):
    #x is initialized above
    x = 1
    while x <= n:
        formula = x * (x + 1) / 2
        print (x,'\t', formula)
        x += 1

print_triangular_numbers(5)
"""

# My solution
def print_triangular_numbers(n):
    for i in range(1, n + 1):
        print(i, "   ", i * (i + 1) / 2)


print(print_triangular_numbers(5))

