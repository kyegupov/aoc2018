from collections import defaultdict
import re
import datetime


s = open('input06')

dots = [] 

for l in s:
    x, y = [int(a.strip()) for a in l.split(',')]
    dots.append((x,y))

matrix = {}
inf = set()

xs = [d[0] for d in dots]
ys = [d[1] for d in dots]

for x in range(min(xs)-1, max(xs)+2):
    for y in range(min(ys)-1, max(ys)+2):
        mr = 99999999
        mi = None
        for i, xy in enumerate(dots):
            xx, yy = xy
            r = abs(x-xx)+abs(y-yy)
            if r == mr:
                mi = None
            if r < mr:
                mr = r
                mi = i
        # print(x,y,mi)
        matrix[(x,y)] = mi
        if x < min(xs) or x > max(xs) or y < min(ys) or y > max(ys):
            inf.add(mi)
print(inf)

count = defaultdict(int)
for v in matrix.values():
    if v not in inf and v != None:
        count[v] += 1

print(max(count.values()))

        


