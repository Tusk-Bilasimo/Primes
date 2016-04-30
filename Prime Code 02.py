n = int(input("Please input a maxValue "))

pairsList = [5]
loopListOne = []
loopListTwo = []

#Create a pairsList of integers adjacent to all the multiples of 6 up to maxValue 
while (pairsList[-1] < n):
    a = pairsList[-1]**2 + (pairsList[-1]*2) # a**2 + (a*2) = b**2 - (b*2)
    pairsList.append(a//pairsList[-1])
    b = pairsList[-1]**2 + (pairsList[-1]*4) # b**2 + (b*4) = c**2 - (c*4)
    pairsList.append(b//pairsList[-1])

# Create a loopListOne, beginning with the first element of the pairsList:-
# (While the squared value is less then maxValue) Square every second element from the pairsList
# and append it to loopListOne
for x in pairsList[::2]:
    if x **2 <= n:
        loopListOne.append(x**2)
        # Now take the same element and add its product of two, to the squared value and append it to loopListOne,
        # to that add the product of four to the previous result and append that. Repeat and append while less then maxValue.
        while (loopListOne[-1] <= n):
            loopListOne.append(x*2 + loopListOne[-1])
            loopListOne.append(x*4 + loopListOne[-1])

# Create a loopListTwo, beginning with the first element of the pairsList:-
# (While the squared value is less then maxValue) Square every second element from the pairsList
# and append it to loopListTwo
for x in pairsList[1::2]:
    if x **2 <= n:
        loopListTwo.append(x**2)
        # Now take the same element and add its product of four, to the squared value and append it to loopListTwo,
        # to that add the product of two to the previous result and append that. Repeat and append while less then maxValue.
        while (loopListTwo[-1] <= n):
            loopListTwo.append(x*4 + loopListTwo[-1])
            loopListTwo.append(x*2 + loopListTwo[-1])

# Combine the two loopLists into a compositeList
compositeList = loopListOne + loopListTwo

# Create a primesList by striping out the composite integers from the pairsList using the compositeList
primesList = [x for x in pairsList if x not in compositeList]

# Add the first two primes into the  primesList
primesList.extend([2,3])
list.sort(primesList)
    
print(primesList)
print("The number of primes in the list is: -")
print(len(primesList))

print('End')


#for i in primesList:
#    print(i)    

