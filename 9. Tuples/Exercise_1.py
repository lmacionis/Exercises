"""
We’ve said nothing in this chapter about whether you can pass tuples as
arguments to a function. Construct a small Python example to test whether
this is possible, and write up your findings.
"""

tuple = ("Lukas", 1995)

# MY ANSWER
def tuple_as_argument(n):
    for i in n:
        print(n)


tuple_as_argument(tuple)

# YES YOU CAN PASS TUPLES AS ARGUMENTS IN A FUNCTION

# FOUND IN A https://stackoverflow.com/questions/6304808/how-to-pass-tuple-as-argument-in-python/6304835
def product(my_tuple):
    for i in my_tuple:
        print(i)

my_tuple = (2,3,4,5)
product(my_tuple)