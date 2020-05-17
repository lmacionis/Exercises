""""
Write a program that reads a file and writes out a new file with the lines in reversed order
(i.e. the first line in the old file becomes the last one in the new file.)
"""
# reads everything into a list of lines
myfile = open("test.txt", "r")
reading_line = myfile.readlines()
myfile.close()

reading_line.reverse()              # reverses the list of lines

# writes reversed list back to another file
new_file = open("test2.txt", "w")
for i in reading_line:
    new_file.write(i)
new_file.close()

# Prints out a second file test2.txt, not necessary for the task.
mynewhandle = open("test2.txt", "r")
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    # Now process the line we've just read
    print(theline, end="")

mynewhandle.close()