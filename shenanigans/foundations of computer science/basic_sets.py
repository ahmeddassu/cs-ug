import math
import random

# a set is an unordered collection containing zero duplicates
def generate_set(length, min, max):
    generated = []
    generated.append(random.randint(min, max))

    for _ in range(length):
        temp = random.randint(min, max)
        if temp in generated:
            continue
        else:
            generated.append(temp)

    return generated

print(generate_set(19, 1, 25))

# they must be the same length, and contain the same elements
# however the order of elements does not matter
# and duplicates do not matter
def is_set_equivalent(a, b):
    if len(a) != len(b):
        return False
          
    for element in a:
        if element not in b:
            return False
            
    return True

# if all elements of the set are in another set 
def is_subset(a, subs):
    if len(subs) > len(a):
        return False

    for element in subs:
        if element in a: continue
        else: return False

    return True

# only a proper subset if the size of the subset is less than that of the set
def is_proper_subset(a, subs):
    if not is_subset(a, subs): return False
    if len(a) == len(subs): return False
    if len(a) > len(subs): return True

# the set of all subsets
# the length of the power_set is always 2^n where n is the number of items in s
def power_set(s):
    pset = []
    pset.append([]) # the empty set is always a subset of any set, but isn't necessarily an element of it
    
    for element in s:
        new_subs = []
        for subset in pset:
            new_subs.append(subset + [element])
        pset.extend(new_subs) # extent adds the elements of the iterable, not the iterable itself
        
    return pset

print(power_set([1, 2, "b", "a"]))

def union(a, b):
    return list(set(a) | set(b))


def intersection(a, b):
    intersect = list(set(a) & set(b))
    
    if not intersect: return "disjoint"
    else: return intersect


def difference(a, b):
    return list(set(a) - set(b))


def absolute_complement(universal, a):
    return difference(universal, a)








