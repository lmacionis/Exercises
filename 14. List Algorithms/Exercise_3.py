"""
Adapt the queens program so that we keep a list of solutions that have already printed,
so that we don’t print the same solution more than once.
"""
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

    bd = list(range(4))     # Generate the initial permutation  With this you can change the size of the bord.
    num_found = 0
    tries = 0
    while num_found < 2:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd) and bd not in list_of_solutions:  # for skipping duplicate solutions, I need to compare them with the list_of_solutions
           print("Found solution {0} in {1} tries.".format(bd, tries))
           list_of_solutions.append(list(bd))   # copy of current solutions
           tries = 0
           num_found += 1

main()
for i in list_of_solutions:
    print(i)