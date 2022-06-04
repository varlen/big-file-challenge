from collections import Counter

ocurrences = Counter()

with open('bigfile.txt', mode='r') as file:
    for line in file:
        ocurrences[line.strip()] += 1

print(dict(ocurrences))