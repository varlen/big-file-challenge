import random
possible_symbols = ['123', 'ABC', 'ZZZ']

with open('bigfile.txt', mode='w') as file:
    for i in range(21_000_000):
        file.write(f"{random.choice(possible_symbols)}\n")
