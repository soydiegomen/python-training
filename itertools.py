#itertools: product, permutations, combinations, accumulate, groupby and infiniy iterators
from itertools import combinations, product, permutations, accumulate, groupby
import operator

def do_product():
    a = [1,2]
    b = [3,4]

    prod = product(a,b)
    print(list(prod))


def do_permutations():
    a = [1,2,3]

    permu = permutations(a)
    print(list(permu))

def do_combinations():
    a = [1,2,3,4,5]

    comb = combinations(a, 2)
    print(list(comb))

def do_accumulate():
    a = [1,2,3,4,5]

    acum = accumulate(a)
    print(list(acum))

    acum = accumulate(a, operator.mul)
    print(list(acum))

    a = [1,2,10,3,11,5]
    acum = accumulate(a, func=max)
    print(list(acum))

def do_groups():
    a = [1,2,3,4,5,6,7,8,9]

    groups = groupby(a, key=lambda x: x > 5)

    for key, value in groups:
        print(key, list(value))

    persons = [
        {'name':'Luis', 'age':12},
        {'name':'Maria', 'age':12},
        {'name':'Carla', 'age':20},
        {'name':'Jorge', 'age':35}
    ]

    groups = groupby(persons, key=lambda x: x['age'])

    for key, value in groups:
        print(key, list(value))

#do_product()
#do_permutations()
#do_combinations()
#do_accumulate()
do_groups()