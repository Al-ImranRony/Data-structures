# list methods:-
# print(dir(list()))

#  Uses of 'in' function
l = [1, 3, 9]
print(3 in l)

# Uses of split method in a file
fname = input("Enter a file name: ")
fhandle = open(fname)

for line in fhandle:
    line = line.rstrip()
    if not line.startswith("often"):
        continue
    words = line.split()
    sliced = words[2]
    pieces = sliced.split("-")  # double split
    print(pieces)
