
# Open help for the math module.
import math
help(math)

# a. How many functions are in the math module? Ats.: 55
import math
for method in dir(math):    # All math functions are printed out
    print(method)
    
# b. What does math.ceil do? What about math.floor? (hint: both floor and ceil expect floating point arguments.)
print(math.ceil(2.3))   # Ats.: 3, this function returns the smallest integral value greater than the number. 
# If number is already integer, same number is returned.
print(math.floor(2.7))  # Ats.: 2, its the opposite of a math.ceil function

# c. Describe how we have been computing the same value as math.sqrt without using the math module.
# Ats.: we can always rise the number by 1/2, for example 4**1/2=2
print(4**1/2)

# d. What are the two data constants in the math module?
# Ats.: pi and e
# Record detailed notes of your investigation in this exercise.