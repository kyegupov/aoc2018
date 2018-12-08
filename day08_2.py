from collections import defaultdict
import re
import datetime


s = open('input08').read()

x = [int(x) for x in s.split()]

child_remains_stack = [1]
meta_remains_stack = [0]
values_stack = [[]]
i = 0
ms = 0
while i < len(x):
    child_remains_stack.append(x[i])
    cn = x[i]
    i+=1
    meta_remains_stack.append(x[i])
    i+=1
    values_stack.append([])
    while child_remains_stack[-1] == 0:
        child_remains_stack.pop()
        value = 0
        # print(values_stack)
        if values_stack[-1]:
            for n in range(meta_remains_stack.pop()):
                # print('ind', x[i], values_stack)
                if x[i] <= len(values_stack[-1]):
                    value += values_stack[-1][x[i]-1]
                i += 1
        else:
            for n in range(meta_remains_stack.pop()):
                # print('d', x[i])
                value += x[i]
                i += 1
        values_stack.pop()
        values_stack[-1].append(value)
    child_remains_stack[-1] -= 1
    # print(child_remains_stack, meta_remains_stack, ms)

print(values_stack)