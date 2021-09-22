# Dictionaries: Key-Values pairs, unordened, mutable

def work_with_dictionaries():
    my_dict = { 'name': 'Diego', 'age': 35, 'city': 'cdmx' }
    print(my_dict)

    second_dict = dict(name='Mary', age=28, city='queretaro')
    print('#second_dic', second_dict)

    #Get value
    print('#Name ', my_dict['name'])

    #Is mutable and we can change/add new key-value
    my_dict['email'] = 'diego@mail.com'
    print('#Add key-value ', my_dict)

    #Delete some key-value
    #my_dict.pop('city')
    del my_dict['age']
    print('#Delete key-value ', my_dict)


    #Remove the las key-value
    last_key, last_value = second_dict.popitem()
    print('#Remove the key-value ', second_dict)
    print('item', last_key, last_value)

    #Check if key exist
    if 'email' in my_dict:
        print('Contains email %s' % my_dict["email"])

    #Loop the keys
    for key in my_dict:
        print(f'#key {key}')

    #Loop values
    for value in my_dict.values():
        print(f'#value {value}')

    #Loop items
    for key, value in my_dict.items():
        print(f'#item {key} - {value}')


def other_dic_functions():
    #Create copy of the dictionary
    my_dict = { 'name': 'Diego', 'age': 35, 'city': 'cdmx' }
    new_dic = my_dict.copy()

    new_dic['email'] = 'jose@mail.com'
    new_dic['name'] = 'Jose'
    print('#Original dic', my_dict)
    print('#Copied dic', new_dic)

    #Update dictionary (add new keys and update new values)
    my_dict.update(new_dic)
    print('#Updated dic', my_dict)

    #Use numbers as a keys
    #Can use an immutable data as a key (tuples)
    square_dic = { 3:9, 4:16, 5:25}
    print('#square_dic ', square_dic)
    print('#square of four ', square_dic[4])


#work_with_dictionaries()
other_dic_functions()