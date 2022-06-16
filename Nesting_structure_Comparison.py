# https://www.codewars.com/kata/520446778469526ec0000001

def same_structure_as(x, y):
    if isinstance(x, list) and isinstance(y, list):
        if len(x) == len(y):
            for index, value in enumerate(x):
                if isinstance(value, list):
                    return same_structure_as(value, y[index])
                elif isinstance(y[index], list):
                    return False
            return True
        else:
            return False
    return False
