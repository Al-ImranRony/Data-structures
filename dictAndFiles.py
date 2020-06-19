# Counting words from a file by dictionary

# counts = dict()
# line = input("Enter a line of words: ")
# words = line.split()
# print("Words: ", words)

# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print("Counts: ", counts)


fname = input("Enter file: ")
fhandle = open(fname)

counts = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# print(counts)
mword = None
mcount = None
for word, count in counts.items():
    if mcount is None or count > mcount:  # Counting-max function
        mword = word
        mcount = count

print(mword, mcount)
