from collections import defaultdict
import re

matrix = defaultdict(int)

re_l = re.compile(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)')

for line in open('input03'):
    x,y,w,h = (int(x) for x in re_l.match(line).groups())
    for dy in range(h):
        for dx in range(w):
            matrix[(x+dx, y+dy)] += 1

for line in open('input03'):
    x,y,w,h = (int(x) for x in re_l.match(line).groups())
    yes = 1
    for dy in range(h):
        for dx in range(w):
            if matrix[(x+dx, y+dy)] > 1:
                yes = 0
    if yes:
        print(line)
        break

