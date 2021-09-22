# Tuple: ordered, inmutable, allows duplicate elements
# Tuples are more efficients than list (is important when you are working with big data)

def tuple_operations():
    #my_tuple = ('x','a','b','x','c','d','e','x')
    my_tuple = ('1','2','3','4','5','6','7','c')

    #Exist some item
    if 'x' in my_tuple:
        print('Yes, X exit')
    else:
        print('No, X exit')

    #Position of an item
    index_c = my_tuple.index('c')
    print('The index C is %d' % index_c)

    #Size of tuple
    print('#Size %d' % len(my_tuple))

    #How many times are X?
    print('#Times "X" %d' % my_tuple.count('x'))

    #Slice tuple
    slice_tuple = my_tuple[-4:]
    print('#Slice ', slice_tuple)

    #Every second element
    seconds_elements = my_tuple[::2]
    print('#Seconds items ', seconds_elements)

    #Reverse the tuple
    inverted_list = my_tuple[::-1]
    print('#Inverted ', inverted_list)

    #Convert to list
    my_list = list(my_tuple)
    print('#Convert to list ', my_list)

    #Convert to tuple again
    new_tuple = tuple(my_list)
    print('#Convert to tuple ', new_tuple)

    #Assign values to variables (you don´t need write the parenthesis)
    person_tuple = 'Diego', 35, 'Mexico'
    name, age, city = person_tuple

    print('#person_tuple', person_tuple)
    print(name, age, city)

    #tick to separate a tuple en variables
    numbers_tuple = (0,1,2,3,4,5)
    first, *middle_values, last = numbers_tuple
    print('#first ', first)
    print('#last ', last)
    print('#middle ', middle_values)

tuple_operations()