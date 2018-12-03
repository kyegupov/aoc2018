clipped = set()

for x in open('input02'):
    x = x.strip()
    for i in range(len(x)):
        z = (x[:i]+x[i+1:], i)
        if z in clipped:
            print(z[0])
        clipped.add(z)
    

