n = int(input("Please input a maxValue "))

primesList = [2,3,5] 
pairsList = [5]

while (pairsList[-1] <= n):
    a = pairsList[-1]**2 + (pairsList[-1]*2) # a**2 + (a*2) = b**2 - (b*2) this "steps" over each multiple of 6
    pairsList.append(a//pairsList[-1]) # this brings the step back to segregated pair value and apends it to pairs list
    for i in pairsList:
        if i <= pairsList[-1] **0.5: # to test for prime factors, we only need to test up to square root of i
            if pairsList[-1] % i == 0: # we only need to test the list items to see if its a prime
                break # if 
        else:
            primesList.append(pairsList[-1])
            break
        
    b = pairsList[-1]**2 + (pairsList[-1]*4) # b**2 + (b*4) = c**2 - (c*4) this "steps" over accross to the next multiple of 6
    pairsList.append(b//pairsList[-1])
    for i in pairsList:
        if i <= pairsList[-1] **0.5:
            if pairsList[-1] % i == 0:
                break
        else:
            primesList.append(pairsList[-1])
            break
            
print(primesList)
print("The number of primes in the list is: -")
print(len(primesList))
