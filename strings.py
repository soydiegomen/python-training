#Strings: ordered, immutable, text representation

def basic_string_functions():
    multi_line = """Uno \
    Dos 
    Tres"""
    print('#Multiline', multi_line)

    my_string = 'Hello world'
    print(my_string)

    #Substring
    char_list = my_string[:5]
    print('#Char list (Substring)', char_list)

    #Clean / Strip string
    dirty_string = '    may spaces             '
    print(dirty_string, 'end')
    print(dirty_string.strip(), 'end')

    #Upper and lower
    print(my_string.upper())
    print(my_string.lower())

def search_functions():
    my_string = 'Hello world'

    #Contains
    if 'world' in my_string:
        print('Contains world')

    if my_string.startswith('Hello'):
        print('Starts with Hello')

    if my_string.endswith('World'):
        print('Ends with world')
    
    index_word = my_string.find('ll')
    print(f'"ll" is in index {index_word}')

    count_letter = my_string.count('o')
    print('There are %d letter "o"' % count_letter)

    print('Replace ', my_string.replace('world', 'Diego'))

def split_and_join_functions():
    my_string = 'how are you doing'
    list_words = my_string.split()
    print('List words ', list_words)

    my_string = 'one,two,three,four'
    list_words = my_string.split(',')
    print('List words ', list_words)

    """#Important: Concat string is not a good practise because the strings are inmutable """
    #Join array string
    concat_string = '-'.join(list_words)
    print(concat_string)

def string_formats():
    name = 'Diego'
    last_name = 'Mendoza'
    age = 35.223333

    #Oldest way
    my_string = 'Name %s' % name
    print(my_string)
    
    #Newes (python 3.6)
    my_string = f'Name {name} {last_name} {age:.2f}'
    print(my_string)

#basic_string_functions()
#search_functions()
#split_and_join_functions()
string_formats()