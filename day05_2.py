from collections import defaultdict
import re
import datetime

s = open('input05').read()

lett = set(s.lower())


minl = len(s)
for l in sorted(lett):
    print(l)

    n = {i:i+1 for i in range(len(s))}
    n[len(s)-1] = None
    n[-1] = 0

    f = True
    while f:
        p = -1
        i = n[p]
        f = False
        while n[i] != None:
            if s[i].lower() == l:
                n[p] = n[i]
                f = True
            elif s[i].lower() == s[n[i]].lower() and s[i] != s[n[i]]:
                # print(s[i], s[n[i]])
                n[p] = n[n[i]]
                f = True
            p = i
            i = n[i]

    c = 0
    i = n[-1]
    ss = ''
    while i != None:
        # ss += s[i]
        i = n[i]
        c+=1
    if c < minl:
        minl = c
    print(minl)





