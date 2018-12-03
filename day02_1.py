from collections import defaultdict

twos = 0
threes = 0

for x in open('input02'):
    y = defaultdict(int)
    for c in x:
        y[c] += 1
    if 2 in y.values():
        twos += 1
    if 3 in y.values():
        threes += 1

print(twos * threes)

