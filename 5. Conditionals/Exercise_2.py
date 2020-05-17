# You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a
# Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting
# day number, and the length of your stay, and it will tell you the name of day of the week you will return on.


def day_nr(n):
    d = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return d[n]


a = 3                   # starting day
b = 137                 # length of stay away
c = day_nr((a + b % 7) % 7)   # day of return
print(c)
