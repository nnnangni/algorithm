E,S,M = map(int,input().split())
year = 0
play = True
while play:
    year += 1
    e = year%15
    s = year%28
    m = year%19
    if e==0:
        e = 15
    if s==0:
        s = 28
    if m==0:
        m = 19
    if e==E and s==S and m==M:
        play=False
print(year)
