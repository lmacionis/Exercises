# Extend the above program so that the sides can be given to the function in any order.


def is_right(x, y, z):
    if x < z and y < z:                     # If z is hypotenuse
        hypot = ((x ** 2 + y **2) ** 0.5)
        if abs(z - hypot) < 0.001:
            return True
        else:
            return False
    elif x < y and z < y:                   # If y is hypotenuse
        hypot = ((x ** 2 + z ** 2) ** 0.5)
        if abs(y - hypot) < 0.001:
            return True
        else:
            return False
    else:                                   # If x is hypotenuse
        hypot = ((y ** 2 + z ** 2) ** 0.5)
        if abs(x - hypot) < 0.001:
            return True
        else:
            return False


print(is_right(5, 7.071, 5))
