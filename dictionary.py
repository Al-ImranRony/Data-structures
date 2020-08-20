# counting on a dictionary

counts = dict()
names = ["Rony", "Imran", "Ali", "Rony"]
fames = {'Cool': 1, 'Patient': 2, 'Ambisious': 3}
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts.get(name, 0) + 1  # Ignoring traceback by 'get' method, see below !
print(counts)

'''
When "get()" is called it checks if the given key exists in the dict.
- If it does exist, the value for that key is returned (e.g. name in counts dict.). 
- If it does not exist then the value of the default argument is returned instead (e.g. 0 defaults in counts dict.)
'''


# Merging 2 dictionaries

mergedDict = {**counts, **fames}
print(mergedDict)