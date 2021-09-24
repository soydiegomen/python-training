from functools import reduce


def basics_with_lambda():
    add10 = lambda x: x+10

    print(add10(5))

    mult =  lambda x,y: x*y
    print(mult(7,5))

def sort_with_lambda():
    points2D = [(1,2),(5,8),(9,2),(2,1)]

    sorted_points = sorted(points2D)
    print('#Default sorted', sorted_points)

    sorted_points = sorted(points2D, key=lambda x:x[1])
    print('#Sorted by Y', sorted_points)

    sorted_points = sorted(points2D, key=lambda x: x[0]+x[1])
    print('#Sorted by sum', sorted_points)


def map_with_lambda():
    my_list = [1,2,5,7,3,5]

    result = map(lambda x: x*2, my_list)
    print('Map x2', list(result))

    result2 = [x*2 for x in my_list]
    print('Map x2 easiest way', list(result2))


def filter_with_lambda():
    my_list = [1,2,5,6,3,4]

    result = filter(lambda x: x%2==0, my_list)
    print ('Filter', list(result))

    result = [x for x in my_list if x%2==0]
    print ('Filter easiest way', list(result))


def reduce_with_lambda():
    my_list = [1,2,3,4]
    
    result = reduce(lambda x,y: x*y, my_list)
    print('Reduce', result)



#basics_with_lambda()
#sort_with_lambda()
#map_with_lambda()
#filter_with_lambda()
reduce_with_lambda()