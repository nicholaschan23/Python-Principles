'''
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
'''
def all_equal(list_input):
    if len(list_input) <= 1:
        return True
    token = list_input[0]
    for item in list_input:
        if item is not token:
            return False
    return True