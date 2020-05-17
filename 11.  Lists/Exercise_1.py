"""
What is the Python interpreter’s response to the following?
list(range(10, 0, -2))
The three arguments to the range function are start, stop, and step, respectively.
In this example, start is greater than stop. What happens if start < stop and step < 0?
Write a rule for the relationships among start, stop, and step.
"""

print(list(range(10, 0, -2)))

# Answer:
# Python interpreter's response: [10, 8, 6, 4, 2]

print(list(range(-10, -2, -2))

# It drops a SyntaxError: unexpected EOF while parsing
# The SyntaxError: unexpected EOF while parsing means that the end
# of your source code was reached before all code blocks were completed

# Rule:
# In a situation where the step value is a negative integer, the start value
# must always be greater than the stop value so you will receive a list counting
# down from start to stop. If the start value is less than the stop value,
# you will receive an empty list.