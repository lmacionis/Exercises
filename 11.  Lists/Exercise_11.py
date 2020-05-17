""""
Suppose you want to swap around the values in two variables.
You decide to factor this out into a reusable function, and write this code:

def swap(x, y):      # Incorrect version
     print("before swap statement: x:", x, "y:", y)
     (x, y) = (y, x)
     print("after swap statement: x:", x, "y:", y)

a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)
Run this program and describe the results. Oops! So it didn’t do what you intended! Explain why not.
Using a Python visualizer like the one at http://netserv.ict.ru.ac.za/python3_viz may help you build a good
conceptual model of what is going on. What will be the values of a and b after the call to swap?
"""


# The x and y are local variables inside that function. They get swapped within the function but not returned,
# so the original x and y remain unchanged.
""""
My answer is that this is because it is a pure function that does not actually modify the parameters used as arguments. 
The line (x,y) = (y,x) actually creates a new tuple object that is modified instead the variables x and y. 
So it will seem like the function works based on the print statements, however; variables x and y 
were never changed to begin with.
"""
# my understanding was that a and b were never modified a new object was just created


def swap(x, y):  # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)


a = ["This", "is", "fun"]
b = [2, 3, 4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)