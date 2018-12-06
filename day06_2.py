from collections import defaultdict
import re
import datetime


s = open('input06')

dots = [] 

for l in s:
    x, y = [int(a.strip()) for a in l.split(',')]
    dots.append((x,y))

xs = [d[0] for d in dots]
ys = [d[1] for d in dots]

import math
ex = int(math.ceil(10000/len(dots)))

ok = 0

for x in range(min(xs)-ex, max(xs)+ex):
    for y in range(min(ys)-ex, max(ys)+ex):
        mr = 0
        for i, xy in enumerate(dots):
            xx, yy = xy
            mr += abs(x-xx)+abs(y-yy)
        if mr < 10000:
            ok += 1

print(ok)