from collections import defaultdict
import re
import datetime


s = open('input08').read()

x = [int(x) for x in s.split()]

child_remains_stack = [1]
meta_remains_stack = [0]
i = 0
ms = 0
while i < len(x):
    child_remains_stack.append(x[i])
    i+=1
    meta_remains_stack.append(x[i])
    i+=1
    print(child_remains_stack, meta_remains_stack, ms)
    while child_remains_stack[-1] == 0:
        child_remains_stack.pop()
        for n in range(meta_remains_stack.pop()):
            ms += x[i]
            print(x[i], ms)
            i += 1
    child_remains_stack[-1] -= 1
    # print(child_remains_stack, meta_remains_stack, ms)

print(ms)