fhandle = open("mbox-short")                             # Read the file
counts = dict()
time = list()
for line in fhandle:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        time.append(words[-2])                           # list of times found in the lines 

for ht in time:
    ht = ht.split(":")
    counts[ht[0]] = counts.get(ht[0], 0) + 1             # Dictionary of hours on the lines

lst = sorted([ (key,val) for key,val in counts.items()]) # Sorting by list comprehension

for k,v in lst:
    print(k, v)
