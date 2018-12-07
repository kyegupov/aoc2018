from collections import defaultdict
import re
import datetime


s = open('input07')

nodes = set()
edges = set()
res = []
for l in s:
    x = l.split()
    edges.add((x[1], x[7]))
    nodes.add(x[1])
    nodes.add(x[7])

while nodes:
    all_rcv = {x[1] for x in edges}
    cand = nodes - all_rcv
    print(cand)
    n = sorted(cand)[0]
    nodes.remove(n)
    edges = {e for e in edges if e[0] != n}
    res.append(n)

print(''.join(res))