"""
Investigate the copy module. What does deepcopy do? In which exercises from last chapter
would deepcopy have come in handy?
Ats.: With the one we used string with lists I think so, not sure.
"""
import copy
help(copy)

"""
A deep copy constructs a new compound object and then, recursively,
      inserts *copies* into it of the objects found in the original.
    
    Two problems often exist with deep copy operations that don't exist
    with shallow copy operations:
    
     a) recursive objects (compound objects that, directly or indirectly,
        contain a reference to themselves) may cause a recursive loop
    
     b) because deep copy copies *everything* it may copy too much, e.g.
        administrative data structures that should be shared even between
        copies
"""