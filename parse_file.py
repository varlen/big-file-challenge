from collections import defaultdict

ocurrences = defaultdict(lambda : 0)

with open('bigfile.txt', mode='r') as file:
    while line := file.readline():
        ocurrences[line.strip()] += 1

print(dict(ocurrences))