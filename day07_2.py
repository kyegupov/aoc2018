from collections import defaultdict
import re
import datetime
import pprint


s = open('input07')

nodes = set()
edges = set()
prereq = defaultdict(set)
res = []
for l in s:
    x = l.split()
    edges.add((x[1], x[7]))
    nodes.add(x[1])
    nodes.add(x[7])
    prereq[x[7]].add(x[1])

workers = [(' ', 0)] * 5

pprint.pprint(sorted(prereq.items()))

done = set()
started = set()
cc = 0
eligible = {n for n in nodes if prereq[n] <= done}

while True:
    for i,w in enumerate(workers):
        if w[1] == 1:
            done.add(w[0])
            eligible = {n for n in nodes if n not in started and prereq[n] <= done}
            workers[i] = (' ', 0)
        elif w[1] > 0:
            workers[i] = (w[0], w[1]-1)
    while eligible and any(w[1] == 0 for w in workers):
        n = sorted(eligible)[0]
        eligible.remove(n)
        started.add(n)
        for i,w in enumerate(workers):
            if w[1] == 0:
                workers[i] = (n, 61 + ord(n) - ord('A'))
                break
    else:
        if all(w[1] == 0 for w in workers):
            break
    # print(cc, workers)
    cc += 1
        
print(cc)
