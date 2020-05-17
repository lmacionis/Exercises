# SAME EXERCISE 4 SECOND TRY STUCK IN THE SAME PLAYS E PART

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


list_of_solutions = []  # Creating list of solutions

def main():
    import random
    global list_of_solutions    # Making list_of_solutions a global variable, that I could use it while printing a list of solutions in line 55.
    rng = random.Random()   # Instantiate a generator

    all_sol = []        # all solutions list
    unique_sol = []     # unique solutions list
    bd = list(range(8))     # Generate the initial permutation  With this you can change the size of the bord.
    num_found = 0
    tries = 0
    while num_found < 92:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           x = bd[:]
           all_sol.append(x)

           #print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1

    unique_sol = all_sol[:]     # copy lists

    print("len solall =", len(all_sol))
    for x in all_sol:
        for q in return_family_of_symmetries(x):
            if x == q:
                unique_sol.remove(x)

    print("len sol =", len(unique_sol))


# a. Write a function to mirror a solution in the Y axis
def mirror_y(sol):
    sol_list = sol
    sol_list.reverse()
    return sol_list

# b. Write a function to mirror a solution in the X axis
def mirror_x(sol):
    sol_list = sol
    sol_list.reverse()
    return sol_list


# c. Write a function to rotate a solution by 90 degrees anti-clockwise, and use this to provide 180 and 270
# degree rotations too.
def ninty_degrees(sol):
    length = len(sol) - 1   # Shows the length of the list, by taking the last index from the list
    sol_2 = sol[:]          # Copies the sol list
    for i, value in enumerate(sol):  # Using enumerate to extract the index and the value from the list
        column = length - value
        sol_2[column] = i
    return sol_2


def one_80(sol):
    sol = ninty_degrees(sol)
    sol = ninty_degrees(sol)
    return sol


def two_70(sol):
    sol = ninty_degrees(sol)
    sol = ninty_degrees(sol)
    sol = ninty_degrees(sol)
    return sol


# d. Write a function which is given a solution, and it generates the family of symmetries for that solution.
# For example, the symmetries of [0,4,7,5,2,6,1,3] are
# [[0,4,7,5,2,6,1,3],[7,1,3,0,6,4,2,5],
#  [4,6,1,5,2,0,3,7],[2,5,3,1,7,4,6,0],
#  [3,1,6,2,5,7,4,0],[0,6,4,7,1,3,5,2],
#  [7,3,0,2,5,1,6,4],[5,2,4,6,0,3,1,7]]

def return_family_of_symmetries(sol):
    family = []
    family_2 = []
    family.append(ninty_degrees(sol))
    family.append(one_80(sol))
    family.append(two_70(sol))

    for x in family:
        family_2.append(mirror_x(x))
        family_2.append(mirror_y(x))

    for x in family_2:
        family.append(x)

    result = remove_duplicates(sol)
    return result


def remove_duplicates(sol):
    result = []
    for e in sol:
        if e not in result:
            result.append(e)
    return result


# e. Now adapt the queens program so it won’t list solutions that are in the same family.
# It only prints solutions from unique families.
main()
