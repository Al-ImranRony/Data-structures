# Methods of tuples
t = tuple()
print(dir(t))

# Comparison within tuples
print((6, 0, 0) > (5, 1, 3))
print((3, 7, 100) > (1, 6, 20000))  # logical !

# Sorting by 'keys' is normal, and sorting by 'values' in dict. can be occured by tuples:

t = {"a": 1, "b": 2, "c": 3, "th": 3}  # key-value tuple
l = list()
for k, v in t.items():
    l.append((v, k))                   # value-key tuple
print(l)

l = sorted(l, reverse=True)
print(l)
