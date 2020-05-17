# FOUND HOW TO DO EXERCISE 4 PART E, BUT WITH PERMUTATIONS, THO THAT DOESNT FIT FOR MY EXERCISE.
# AND ITS FROM DIMITRI :D
# Dimitri Frederick
# nqueens.py

from itertools import permutations

# rotations
def rotate(p):
    n = len(p)
    tp = [0] * n
    for i in range(n):
        tp[p[i]] = n - i - 1
    return tp

# reflections
def reflect(p):
    n = len(p)
    rp = [0] * n
    for i in range(n):
        rp[p[i]] = i
    return rp

def get_distinct():
	columns = range(8)
	solutions=[]
	# permutation of columns
	for permutation in permutations(columns):
		#check is diagonally safe and append
		if (8 == len(set(permutation[i] + i for i in columns))
			  == len(set(permutation[i] - i for i in columns))):
			solutions.append(list(permutation))
	return solutions

def get_unique(solutions):
	_sol=solutions[:]
	unique =[]

	while len(_sol) != 0:
		pos = _sol[0]
		unique.append(pos)
		#perform symmetry operations and remove duplicates
		for i in (pos,
				  rotate(pos),
				  rotate(rotate(pos)),
				  rotate(rotate(rotate(pos))),
				  reflect(pos),
				  rotate(reflect(pos)),
				  rotate(rotate(reflect(pos))),
				  rotate(rotate(rotate(reflect(pos))))):
			try:
				_sol.remove(i)
			except:
				pass
	return unique

distinctSolutions = []
uniqueSolutions   = []
distinctSolutions = get_distinct()
uniqueSolutions =get_unique(distinctSolutions)

print("unique solutions:",len(uniqueSolutions))
for sol in uniqueSolutions:
	print(sol)