
sum = 0
ss = set()
f = 0
while not f: 
    for x in open('input01'):
        xx = int(x)
        sum += xx
        if sum in ss:
            print(sum)
            f = 1
            break
        ss.add(sum)

