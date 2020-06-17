fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

print(sorted(lst))

# c = 0
# for line in fh:
#     line = line.rstrip()
#     if line.startswith("From") and not line.startswith("From:"):
#         c += 1
#         words = line.split()
#         print(words[1])
# print(c)
