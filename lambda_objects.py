from functools import reduce

def create_list():
    persons = [
        { 'name': 'Luis', 'age': 22},
        { 'name': 'Pedro', 'age': 15},
        { 'name': 'Maria', 'age': 35},
        { 'name': 'Noemi', 'age': 17},
        { 'name': 'Fernando', 'age': 18},
    ]

    return persons

def sort_objects_list():
    persons = create_list()
    result = sorted(persons, key= lambda x: x['age'])
    print(result)


def map_objects_list():
    persons = create_list()
    result = [ 'Name: '+x['name'] for x in persons]
    print(result)

    result = [ { 'name': x['name'], 'is_adult': (x['age'] >= 18)  } for x in persons]
    print(result)

def filter_objects_list():
    persons = create_list()
    result = [ x for x in persons if x['age'] >=18]
    print('Adults ', result)

def reduce_objects_list():
    persons = create_list()

    def sum_ages(accum, y):
        if(isinstance(accum, int)):
            return accum + y['age']
        else:
            #Just the first time acum is an object, the next is an int
            return accum['age'] + y['age']

    result = reduce(sum_ages, persons)
    print('Ages sum ', result)


#sort_objects_list()
#map_objects_list()
#filter_objects_list()
reduce_objects_list()