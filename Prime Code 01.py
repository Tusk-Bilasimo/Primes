
print("Solving for primes without division")

maxValue = int(input("Please input a maxValue "))

def pair(n): # return pairs (multipile of 6-1 and 6+1) in series up to n
    result = []
    a = 6-1
    b = 6+1
    while a <= n:
        result.append(a)
        a = a+6
        result.append(b)
        b = b+6
    return result

pairsList = pair(maxValue)

newList = [] # A new list to contain the stripped out composite numbers
listPlace = 0
listItem = pairsList[listPlace]
composite = listItem**2

while (composite<=maxValue):
    listItem = pairsList[listPlace]
    composite = listItem**2
    next01 = (listItem*2) + composite
    newList.append(composite)

    while (newList[-1]<=maxValue):
        next01 = (listItem*2) + newList[-1]
        newList.append(next01)
        next02 = (listItem*4) + newList[-1]
        newList.append(next02)

    listPlace = listPlace + 1

    listItem = pairsList[listPlace]
    composite = listItem**2
    next03 = (listItem*4) + composite
    next04 = (listItem*2) + next03

    newList.append(composite)


    while (newList[-1]<maxValue):
        next03 = (listItem*4) + newList[-1]
        newList.append(next03)
        next04 = (listItem*2) + newList[-1]
        newList.append(next04)

    listPlace = listPlace + 1



almostList = [x for x in pairsList if x not in newList]
firstPair = [2,3] # We must remember to retrieve the first true prime pair 2 and 3 *
primeList = firstPair + almostList

print("List of pime numbers")
print(primeList)
print("The number of primes in the list is: -")
print(len(primeList))

print('End')

# *
'''
It begins with the only true prime pair 2 and 3, whose product forms the magical composite number 6. 
All other primes orbit around it and its multiples. Using alternating patterns of 2 and 4, 
the composites are revealed in succession beginning with 5 in the first segregated pair of the series. 
Each integer in the series is raised to the second power and then its product of 2 and 4 reveals the distribution of the composite numbers.
As the process is repeated, the order that 2 and 4 are used to generate the products alternates, 
to progressively strip away the remaining composites integers and reveal the rest of the primes. 
'''
# for i in primeList:
#       print(i)    


