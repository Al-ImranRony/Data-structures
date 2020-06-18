# counting on a dictionary

counts = dict()
names = ["Rony", "Imran", "Ali", "Rony"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts.get(name, 0) + 1  # Ignoring traceback by 'get' method
print(counts)
