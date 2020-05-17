# Write a fruitful function sum_to(n) that returns the sum of all integer
# numbers up to and including n. So sum_to(10) would be 1+2+3...+10 which would return the value 55.


def sum_to(n):
    """ Formula that returns the sum of all integer
    numbers up to and including n """
    x = (n * (n + 1)) / 2
    return x                        # This is new, and makes the function fruitful.


# now that we have the function above, let us call it.
n = int(input("Number: "))          # Input of any number
x = sum_to(n)                       # Calling a function and applying to x
print(x)                            # Answer