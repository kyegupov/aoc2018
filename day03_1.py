from collections import defaultdict
import re

matrix = defaultdict(int)

re_l = re.compile(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)')

for line in open('input03'):
    x,y,w,h = (int(x) for x in re_l.match(line).groups())
    for dy in range(h):
        for dx in range(w):
            matrix[(x+dx, y+dy)] += 1

c = 0
for v in matrix.values():
    if v >= 2:
        c += 1

print(c)
