name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1

mword = None
mcount = None
for word, count in counts.items():
    if mcount is None or count > mcount:
        mword = word
        mcount = count
print(mword, mcount)
