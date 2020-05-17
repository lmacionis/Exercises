"""
Add a print function to Newton’s sqrt function that prints out better each
time it is calculated. Call your modified function with 25 as an argument
and record the results.

Did not understood this exercises
"""

# Newton's method for finding square roots
def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better


# Answer from google
def newtonSqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:
        approx = better
        better = (approx + n/approx)/2.0
        print("Approx:", better)
    return approx


print("Final approx:", newtonSqrt(25))


# Test cases
print(sqrt(25.0))
print(sqrt(49.0))
print(sqrt(81.0))