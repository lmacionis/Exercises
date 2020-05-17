# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
# Write a function which is given the day number, and it returns the day name (a string).


def day_nr(n):
    if n == 0:
        print("Sun")
    elif n == 1:
        print("Mon")
    elif n == 2:
        print("Tue")
    elif n == 3:
        print("Wed")
    elif n == 4:
        print("Thu")
    elif n == 5:
        print("Fri")
    elif n == 6:
        print("Sat")
    else:
        print("Not a valid number")


n = int(input("Please choose the number between 0 and 6: "))

day_nr(n)
