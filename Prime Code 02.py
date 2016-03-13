n = int(input("Please input a maxValue "))

pairsList = [5]
loopListOne = []
loopListTwo = []

while (pairsList[-1] < n):
    a = pairsList[-1]**2 + (pairsList[-1]*2) # a**2 + (a*2) = b**2 - (b*2)
    pairsList.append(a//pairsList[-1])
    b = pairsList[-1]**2 + (pairsList[-1]*4) # b**2 + (b*4) = c**2 - (c*4)
    pairsList.append(b//pairsList[-1])
    
for x in pairsList[::2]:
    if x **2 <= n:
        loopListOne.append(x**2)
        while (loopListOne[-1] <= n):
            loopListOne.append(x*2 + loopListOne[-1])
            loopListOne.append(x*4 + loopListOne[-1])

for x in pairsList[1::2]:
    if x **2 <= n:
        loopListTwo.append(x**2)
        while (loopListTwo[-1] <= n):
            loopListTwo.append(x*4 + loopListTwo[-1])
            loopListTwo.append(x*2 + loopListTwo[-1])

compositeList = loopListOne + loopListTwo

primesList = [x for x in pairsList if x not in compositeList]
primesList.extend([2,3])
list.sort(primesList)
    
print(primesList)
print("The number of primes in the list is: -")
print(len(primesList))

print('End')


#for i in primesList:
#      print(i)    



