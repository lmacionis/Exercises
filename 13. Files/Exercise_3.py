"""
Write a program that reads a text file and produces an output file which is a copy of the file,
except the first five columns of each line contain a four digit line number, followed by a space.
Start numbering the first line in the output file at 1. Ensure that every line number is formatted
to the same width in the output file. Use one of your Python programs as test data for this exercise:
your output should be a printed and numbered listing of the Python program.
"""

# tried to solve it for 8hours couldnt make it, so just copied from https://forum.ubuntu.com.cn/viewtopic.php?t=401287
# and just figure out how it works.
# looks simple enough, but either im stupid or I dont get something.
def add_line_number(oldfile, newfile):
    handleoldfile = open(oldfile, "r")
    handlenewfile = open(newfile, "w")
    count = 1
    while True:
        oldline = handleoldfile.readline()
        if len(oldline) == 0:
            break
        newline = "{0:>4}".format(str(count)) + " " + oldline
        handlenewfile.write(newline)
        count += 1
    handleoldfile.close()
    handlenewfile.close()


add_line_number("exercise_2_snake.txt", "newfile.txt")