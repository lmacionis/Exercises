"""
Write a program that reads a file and prints only those lines that contain the substring snake.
"""

my_file = open("exercise_2_snake.txt")      # opens the file
for line in my_file:        # takes every line
    if "snake" in line:     # checks if line has a word snake
        print(line)         # prints the line which contains word snake

my_file.close()             # closes the file