
"""
This is the "nester.py" module, 
and it provides one funtion called print_lol() 
which prints list that may or may not include nested list.
"""


def print_lol(the_list):
    """
    This function takes a positional parameter called "the_list". 
    which is any Python list (of, possibly, nested lists).
    Each data item in the provided list is (recursively) printed to the screen on its own line.
    """
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

# movies = ['\"A\"', 'B', 'C', [1, 2, 3]]
# movies.insert(1, 1981)
# movies.insert(3, 1971)
# movies.insert(5, 1985)
# movies.insert(5, [1, 9, ["x", "y", "z"], 8, 5])
# print (movies)
# print ("===================================")
# print_lol(movies)

