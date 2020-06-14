# Opening a file

fname = input("Enter the file name: ")
f = open(fname)
c = 0
for line in f:
    line = line.rstrip()
    if line.startswith("Python"):
        c = c + 1
print("There are", c, "line which starts with python")
