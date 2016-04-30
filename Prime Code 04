n = int(input("Please input a maxValue "))

primesList = []

# We test all the integers immediately below a multiple of 6
# Begining with 5 up to maxValue
for x in range (5, n + 1, 6):
    isPrime = True
    # We only need to test for primeness up the square root of that value
    for i in range (5, int(x **0.5) + 1):
        if x % i == 0:
            isPrime = False
            # as soon as it fails we can quit the loop
            break

    if isPrime:
        primesList.append(x)
        
# We test all the integers immediately above a multiple of 6
# Begining with 7 up to maxValue
for y in range (7, n + 1, 6):
    isPrime = True
    for i in range (5, int(y **0.5) + 1):
        if y % i == 0:
            isPrime = False
            break

    if isPrime:
        primesList.append(y)
        
primesList.extend([2,3])   
list.sort(primesList)
print(primesList)
print("The number of primes in the list is: -")
print(len(primesList))

print('End')
