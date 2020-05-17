"""
Every week a computer scientist buys four lotto tickets. She always chooses the same prime numbers,
with the hope that if she ever hits the jackpot, she will be able to go onto TV and Facebook
and tell everyone her secret. This will suddenly create widespread public interest in prime numbers,
and will be the trigger event that ushers in a new age of enlightenment. She represents her weekly
tickets in Python as a list of lists:
my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]
Complete these exercises.
a. Each lotto draw takes six random balls, numbered from 1 to 49. Write a function to return a lotto draw.
b. Write a function that compares a single ticket and a draw, and returns the number of correct picks on that ticket:
test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
c. Write a function that takes a list of tickets and a draw, and returns a list telling how many picks were correct on each ticket:
test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])
d. Write a function that takes a list of integers, and returns the number of primes in the list:
test(primes_in([42, 4, 7, 11, 1, 13]) == 3)
e. Write a function to discover whether the computer scientist has missed any prime numbers in her selection of the four tickets. Return a list of all primes that she has missed:
test(prime_misses(my_tickets) == [3, 29, 47])
f. Write a function that repeatedly makes a new draw, and compares the draw to the four tickets.
    i. Count how many draws are needed until one of the computer scientist’s tickets has at least 3 correct picks.
    Try the experiment twenty times, and average out the number of draws needed.
    ii. How many draws are needed, on average, before she gets at least 4 picks correct?
    iii. How many draws are needed, on average, before she gets at least 5 correct? (Hint: this might take a while.
    It would be nice if you could print some dots, like a progress bar, to show when each of the
    20 experiments has completed.)
Notice that we have difficulty constructing test cases here, because our random numbers are not deterministic.
Automated testing only really works if you already know what the answer should be!
"""

# a. Each lotto draw takes six random balls, numbered from 1 to 49. Write a function to return a lotto draw.
my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

mylist = []

def lotto_draw():
    import random
    list_size = 0
    mylist.clear()  # clearing the list that it always would be empty.
    while list_size < 6:
        x = random.randint(1, 49)
        if x not in mylist:
            mylist.append(x)
            list_size += 1

    return mylist


lotto_draw()
print(mylist)

# b. Write a function that compares a single ticket and a draw, and returns the number of correct picks on that ticket:
# test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
def compare_tick(tick):
    draw_nr = mylist
    correct_picks = 0
    for x in draw_nr:
        for y in tick:
            if x == y:
                correct_picks += 1
    return correct_picks


tick = [42,4,7,11,1,13]
compare_tick(tick)

# c. Write a function that takes a list of tickets and a draw, and returns a list telling
# how many picks were correct on each ticket:
# test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])
def lotto_matches(tick):
    correct_pick_list = []
    tick = my_tickets
    for x in tick:
        correct_pick_list.append(compare_tick(x))
    return print(correct_pick_list)


lotto_matches(my_tickets)

# d. Write a function that takes a list of integers, and returns the number of primes in the list:
# test(primes_in([42, 4, 7, 11, 1, 13]) == 3)
def prime_in(list):
    num_of_primes = 0
    import math
    for x in list:
        if x > 1:
            for i in range(2, int(math.sqrt(x))):
                if (x % i) == 0:
                    break
            else:
                num_of_primes += 1
        else:
            break
    return print(num_of_primes)


list = [42, 4, 7, 11, 1, 13]
prime_in(list)

# e. Write a function to discover whether the computer scientist has missed any prime numbers
# in her selection of the four tickets. Return a list of all primes that she has missed:
# test(prime_misses(my_tickets) == [3, 29, 47])
def prime_misses(list):
    list_of_prime = []
    for prime_nr in range(1, 50):
        if prime_nr > 1:
            for n in range(2, prime_nr):
                if (prime_nr % n) == 0:
                    break
            else:
                list_of_prime.append(prime_nr)
    for x in list:
        for y in x:
            if y in list_of_prime:
                list_of_prime.remove(y)
            else:
                continue
    return print(list_of_prime)


prime_misses(my_tickets)

# f. Write a function that repeatedly makes a new draw, and compares the draw to the four tickets.
#     i. Count how many draws are needed until one of the computer scientist’s tickets has at least 3 correct picks.
# don't even know why I put so many comments here :D
def new_draw(times_to_run_loop):
    draw_you_need = 0
    correct_numb = 0
    while correct_numb < times_to_run_loop:     # running a while loop 3 times, like exercise says
        lotto_draw()    # calling lotto_draw for new random list
        for x in my_tickets:    # creating a list from a matrix my_tickets
            correct_numb = 0    # reassigning correct_numb for a new list from a matrix my_tickets
            for y in x:         # taking a number from list x
                if y in mylist:  # checking if a number is in a lotto draw or a random list
                    correct_numb += 1   # counting how many numbers was guested
                    if correct_numb != times_to_run_loop:   # if we don't have 3 correct numbers we are taking a new list from a matrix
                        continue
                    else:       # if we guested 3 numbers, we are adding 1 to times we needed to
                        # guess the correct numbers and printing it out
                        draw_you_need += 1
                        return draw_you_need
                else:   # if number y(from matrix list) not in a lotto draw(mylist), taking a new number from list x
                    continue

        if correct_numb != times_to_run_loop:   # if we did not guested 3 numbers,
            # we are adding 1 to times we needed to guess and rerunning the while loop
            draw_you_need += 1


new_draw(3)    # calling a function 3 times like asked in i part

#     Try the experiment twenty times, and average out the number of draws needed.
def average_draws(correct_numbers):
    lotto_run_times = 0
    list_of_draws = []
    print_counter = 0
    while lotto_run_times <= 20:
        draws_times = new_draw(correct_numbers)
        list_of_draws.append(draws_times)
        if lotto_run_times == 20:
            average_draws_needed = sum(list_of_draws) / len(list_of_draws)
            return print(average_draws_needed)
        else:
            lotto_run_times += 1


average_draws(3)    # calling a function 3 times like asked in i part
#   ii. How many draws are needed, on average, before she gets at least 4 picks correct?
average_draws(4)    # calling a function 4 times like asked in i part
#    iii. How many draws are needed, on average, before she gets at least 5 correct? (Hint: this might take a while.
average_draws(5)    # calling a function 5 times like asked in i part

# I dont know where should I print out those dots.
#     It would be nice if you could print some dots, like a progress bar, to show when each of the
#     20 experiments has completed.)