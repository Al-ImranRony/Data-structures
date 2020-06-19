# Finding the top 10 most common words of the file

fhandle = open("romeo.txt")
counts = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# lst = list()
# for key, val in counts.items():
#     t = (val, key)
#     lst.append(t)
# lst = sorted(lst, reverse=True)
lst = sorted([ (v,k) for k,v in counts.items()], reverse=True)   #One liner by list-comprehension

for val, key in lst[:10]:       # As lst is in val->key formation now!
    print(key, val)