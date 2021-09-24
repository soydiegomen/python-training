def create_list():
    persons = [
        { 'name': 'Luis', 'age': 22},
        { 'name': 'Maria', 'age': 35},
        { 'name': 'Pedro', 'age': 15},
        { 'name': 'Noemi', 'age': 17},
    ]

    return persons

def do_something_cool():
    persons = create_list()

    #Iterate
    for person in persons:
        print(person['name'])

    #Exist item in list
    res = any(person['age'] == 27 for person in persons )
    if res:
        print('Yes, 27 is in the list')
    else:
        print('No, 27 is not in the list')
    
    #Find someone
    #list_result = [person for person in persons if person['age'] >= 22]
    list_result = [person for person in persons if person['name'] == 'Maria']
    print('#Find Item', list_result)

    
    #Sort using their ages
    #persons.sort(key=lambda x: x['age'], reverse=True)
    persons.sort(key=lambda x: x['age'])
    print('#sorted', persons)

    #Copy a list
    persons_copy = persons.copy()
    persons.clear()
    print('#Original list: ', persons)
    print('#Copied list: ', persons_copy)

    #Operations with items in list
    result = [ { 'name': person['name'], 'is_adult': (person['age'] >= 18) } for person in persons_copy]
    print('#operation: ', result)


do_something_cool()