# Function argument unpacking

import sys

def aFunc(x, y, z):
    return(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

print(aFunc(*tuple_vec))

print(aFunc(**dict_vec))
