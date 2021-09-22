#Sets: unordered, mutable, no duplicates

def basics_with_sets():
    #my_set = set('Hello')
    my_set = {1,2,3,4,5}

    my_set.add(6)
    my_set.remove(3)
    #my_set.remove(8) #Throw a error
    my_set.discard(8)
    first_item = my_set.pop()
    print('#First ', first_item)

    print(my_set)

    #Iterate
    for i in my_set:
        print(i)
    
    #Check if exist
    if 5 in my_set:
        print('5 exist in set')

def functions_with_sets():
    odds = {1,3,5,7,9}
    evens = {0,2,4,6,8}
    primes = {2,3,5,7}

    #Union
    union = odds.union(evens)
    print('#Union', union)

    #Intersection
    intersection = odds.intersection(primes)
    print('#Intersection (primes)', intersection)

    #Differences
    differences = odds.difference(primes)
    print('#Differences ', differences)

    #Symmetric differences
    sym_diff = odds.symmetric_difference(primes)
    print('#Symmetric difference', sym_diff)

    #Update
    new_set = {7,9,11,13,15}
    new_set.update(odds)
    print('#Update', new_set)

    #Intersect update
    new_set = {7,9,11,13,15}
    new_set.intersection_update(odds)
    print('#Intersection update', new_set)

    #Difference update
    new_set = {7,9,11,13,15}
    new_set.difference_update(odds)
    print('#Difference update', new_set)


def last_part_sets():
    set_a = {1,2,3,4,5,6}
    set_b = {1,2,3}

    print('Is b subset of a', set_b.issubset(set_a))

    print('Is a superset of b', set_a.issuperset(set_b))

    #frozenset: is a inmutable set
    my_set = frozenset([1,2,3,4,5,6])
    #my_set.add(7)
    #my_set.remove(1)
    print('Frozenset', my_set)

#basics_with_sets()
#functions_with_sets()
last_part_sets()
