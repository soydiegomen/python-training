#!/usr/bin/env python3
def sayHello(name):
    print(f'Hello {name}')


def operations_list():
    list_numbers = [9,7,1,2,3,4]

    #Size
    print('List size %d ' % len(list_numbers))

    #A range of items
    print(list_numbers[2:5])
    #First items
    print(list_numbers[:2])
    #Last
    print(list_numbers[-1])
    #Invertir
    print(list_numbers[::-1])

    #Add new item to the end
    list_numbers.append(10)
    print(list_numbers)

    #Remove
    list_numbers.pop() #Remove the last
    list_numbers.remove(2) #Remove some element

    #Iterar
    for number in list_numbers:
        print(number)

    #Exist in list
    if 10 in list_numbers:
        print('Yes it exist')
    else:
        print('Not exist')

    #Concat a list
    new_list = [11,12,5]
    final_list = list_numbers + new_list
    print(final_list)

    #Sort he list
    final_list.sort()
    print(final_list)

    #Copy a list
    copied_list = final_list.copy()
    copied_list.append(100)
    print(final_list)
    print(copied_list)

    #Create a new list using the original list and operation
    square_list = [ item * item for item in copied_list ]
    print(square_list)

    #Count items of the same type
    new_list = [1,2,3,4,5,6,1,2,3,4,5,6,1]
    print('There are %d items with "1"' % new_list.count(1))

operations_list()



