"""
Write a program that undoes the numbering of the previous exercise:
it should read a file with numbered lines and produce another file without line numbers.
"""

# Some parts are copied some writen by me.
numberate_file = open("newfile.txt")
not_numbered_file = open("filewithoutlinenumbers.txt", "w")
while True:
    oldline = numberate_file.readline()
    if len(oldline) == 0:
        break
    newline = ''.join([i for i in oldline if not i.isdigit()])      # removes all numbers from a file
    newlist = newline.replace(" ", "")      # one of the way to remove whitespaces in the start off the line


    not_numbered_file.write(newlist)

numberate_file.close()
not_numbered_file.close()