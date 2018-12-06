from collections import defaultdict
import re
import datetime

mins = defaultdict(int)
min_sleep_guard = defaultdict(lambda: defaultdict(int))
duty = None
sleep = None

re_l = re.compile(r'\[([^\]]+)\] (.+)')

lines = list(open('input04'))
lines.sort()
for l in lines:
    dat, event = re_l.match(l.strip()).groups()
    dt = datetime.datetime.strptime(dat, '%Y-%m-%d %H:%M')
    if event.startswith('Guard'):
        duty = event.split()[1]
    if 'asleep' in event:
        sleep = dt
    if 'wakes' in event:
        mins[duty] += (dt - sleep).seconds / 60
        m2 = dt.minute
        m = sleep.minute
        while m != m2:
            min_sleep_guard[m][duty] += 1
            m += 1
            m %= 60

mx = 0
mm = 0
mg = 0
for m, v in min_sleep_guard.items():
    for g, vv in v.items():
        if vv > mx:
            mm = m
            mg = g
            mx = vv
            
print(mm*int(mg[1:]))

    