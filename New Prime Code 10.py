n = 123


primeList = [2,3,5,7]

h = 7

while (primeList[-1] < n):   
    a = 42 + h
    if a % 49 == 0:
        if a % 343 != 0:
            primeList.append(a//49)
    
    b = 28 + a
    if b % 49 == 0:
        if b % 343 != 0:
            primeList.append(b//49)
    
    c = 14 + b
    if c % 49 == 0:
        if c % 343 != 0:
            primeList.append(c//49)
    
    d = 28 + c
    if d % 49 == 0:
        if d % 343 != 0:
            primeList.append(d//49)
    
    e = 14 + d
    if e % 49 == 0:
        if e % 343 != 0:
            primeList.append(e//49)
    
    f = 28 + e
    if f % 49 == 0:
        if f % 343 != 0:
            primeList.append(f//49)
    
    g = 42 + f
    if g % 49 == 0:
        if g % 343 != 0:
            primeList.append(g//49)
    
    h = 14 + g
    if h % 49 == 0:
        if h % 343 != 0:
            primeList.append(h//49)

primeList.remove(1)    
print(primeList)
print(len(primeList))

