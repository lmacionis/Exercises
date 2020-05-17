"""
The section in this chapter called Alice in Wonderland, again! started with the observation that the merge
algorithm uses a pattern that can be reused in other situations. Adapt the merge algorithm to write
each of these functions, as was suggested there:

a. Return only those items that are present in both lists.
b. Return only those items that are present in the first list, but not in the second.
c. Return only those items that are present in the second list, but not in the first.
d. Return items that are present in either the first or the second list.
e. Return items from the first list that are not eliminated by a matching element in the second list.
In this case, an item in the second list “knocks out” just one matching item in the first list.
This operation is sometimes called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11])
would return [5,11,11,12,13]
"""

# a. Return only those items that are present in both lists.
# I think this is the correct way of doing it. Thou not sure.
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result         # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        # Both lists still have items, copy smaller item to result and add present to result
        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] <= ys[yi]:
            xi += 1
        else:
            yi += 1


xs = [1,3,3,4,5,7,9,11,13,15,17,19,24]
ys = [4,5,8,12,16,20,24]
zs = xs+ys
zs.sort()
print(merge(xs, ys))


# b. Return only those items that are present in the first list, but not in the second.
# I think that I misunderstood the condition and returned the duplicates when I needed to remove them
# Lower you will find the right result.
# If the the a part is good, then this is also good.
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    most_recent_elem = None

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result         # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        # Adding duplicates to result
        if xs[xi] != most_recent_elem:
            most_recent_elem = xs[xi]
        elif xs[xi] == most_recent_elem:    # Or you can just use else
            result.append(xs[xi])
            most_recent_elem = xs[xi]

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            xi += 1
        else:
            xi += 1
            yi += 1


xs = [1,3,3,4,5,7,9,11,11,13,15,17,19,19]
ys = [4,5,8,12,16,20,24]
zs = xs+ys
zs.sort()
print(merge(xs, ys))

# b. Return only those items that are present in the first list, but not in the second.
# This algorithm compares two lists, removes matching elements from the first list and prints it out.
# I think I needed only to return the first lists elements, but thought it's was too simple
# and that's why I misunderstood the condition
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    most_recent_elem = None

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(xs[xi:])
            return result         # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

            # Both lists still have items, copy smaller and present item to result.
        most_recent_elem = ys[yi]
        if xs[xi] != most_recent_elem:
            if ys[yi] <= xs[xi]:
                yi += 1
            else:
                result.append(xs[xi])
                xi += 1
        else:
            xi += 1
            yi += 1

xs = [1,3,3,4,5,7,9,11,11,13,15,17,19,19,24,30,40]
ys = [4,5,8,12,16,20,24,30]
zs = xs+ys
zs.sort()
print(merge(xs, ys))

# c. Return only those items that are present in the second list, but not in the first.
# I think that I misunderstood the condition and returned the duplicates when I needed to remove them
# Lower you will find the right result.
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    most_recent_elem = None

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result         # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        # Adding duplicates to result
        if ys[yi] != most_recent_elem:
            most_recent_elem = ys[yi]
        else:
            result.append(ys[yi])
            most_recent_elem = ys[yi]

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            xi += 1
            yi += 1
        else:
            yi += 1


xs = [1,3,3,4,5,7,9,11,11,13,15,17,19]
ys = [4,4,5,8,8,12,16,20,24,24]
zs = xs+ys
zs.sort()
print(merge(xs, ys))

# c. Return only those items that are present in the second list, but not in the first.
# This algorithm compares two lists, removes matching elements from the second list and prints it out.
# I think I needed only to return the seconds lists elements, but thought it's was too simple
# and that's why I misunderstood the condition.
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    most_recent_elem = None

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:])
            return result         # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(ys[yi:])
            return result

            # Both lists still have items, copy smaller and present item to result.
        most_recent_elem = xs[xi]
        if ys[yi] != most_recent_elem:
            if xs[xi] <= ys[yi]:
                xi += 1
            else:
                result.append(ys[yi])
                yi += 1
        else:
            xi += 1
            yi += 1


xs = [1,3,3,4,5,7,9,11,11,13,15,17,19,19,24,40]
ys = [4,5,8,12,16,20,24,30]
zs = xs+ys
zs.sort()
print(merge(xs, ys))

# d. Return items that are present in either the first or the second list.
# I think that's it, but it looks to easy
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(xs[xi:]) # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1

xs = [1,3,3,4,5,7,9,11,11,13,15,17,19]
ys = [4,4,5,8,8,12,16,20,24,24]
zs = xs+ys
zs.sort()
print(merge(xs, ys))

# e. Return items from the first list that are not eliminated by a matching element in the second list.
# That what I thought I was asked to do in b, c parts.
def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    most_recent_elem = None

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(xs[xi:])
            return result         # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

            # Both lists still have items, copy smaller and present item to result.
        most_recent_elem = ys[yi]
        if xs[xi] != most_recent_elem:
            if ys[yi] <= xs[xi]:
                yi += 1
            else:
                result.append(xs[xi])
                xi += 1
        else:
            xi += 1
            yi += 1

xs = [5,7,11,11,11,12,13]
ys = [7,8,11]
zs = xs+ys
zs.sort()
print(merge(xs, ys))
