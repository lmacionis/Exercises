# Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to this
# scheme:

"""
    Mark        Grade
    >= 75       First
    [70-75)     Upper Second
    [60-70)     Second
    [50-60)     Third
    [45-50)     F1 Supp
    [40-45)     F2
    < 40        F3

The square and round brackets denote closed and open intervals.
A closed interval includes the number, and open interval excludes it.
So 39.99999 gets grade F3, but 40 gets grade F2. Assume

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                     49.9, 45, 44.9, 40, 39.9, 2, 0]

Test your function by printing the mark and the grade for all the elements in this list.
"""

xs = [83, 75, 14.9, 70, 69.9, 65, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]


def grade(m):
    g = ["First", "Upper Second", "Second", "Third", "F1 Supp", "F2", "F3"]

    if 75 <= m:
        return g[0]
    elif 70 <= m and 75 > m:
        return g[1]
    elif m >= 60 and m < 70:
        return g[2]
    elif m >= 50 and m < 60:
        return g[3]
    elif m >= 45 and m < 50:
        return g[4]
    elif m >= 40 and m < 45:
        return g[5]
    else:
        return g[6]


for m in xs:
    print(float(m), "   ", grade(m))
