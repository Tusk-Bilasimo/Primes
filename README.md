#Primes and their Distribution

DESCRIPTION

It begins with 2 the only positive prime and followed with 3 making the only true prime pair 2 and 3, whose sum is the next prime and the beginning of a mysterious sequence, but more importantly their product forms the magical composite number 6. All other primes orbit around it and its multiples. Using alternating patterns of 2 and 4, the composites are revealed in succession beginning with 5 in the first segregated pair of the series. Each integer in the series is raised to the second power and then its product of 2 and 4 reveals the distribution of the composite numbers. As the process is repeated throughout the series, the order that 2 and 4 are used to generate the products alternates, to progressively strip away the remaining composite integers and reveal the rest of the primes.

THE SEGREGATED PAIRS LIST 

Other than 2 and 3 all prime numbers are located adjacent to a multiple of 6, this means we can ignore other integers  in our search for primes.

The following expression can be used and repeated to generate a segregated pairsList of multiples of 6-1 and 6+1. Beginning with:- 

a = 5 

a² + (a x 2) = b² - (b x 2) 

b² + (b x 4) = c² – (c x 4) 

c² + (c x 2) = d² - (d x 2) 

d² + (d x 4) = e² – (e x 4)...........

When setting a maxValue of 100, this generates the following segregated pairsList:- 

[5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 59, 61, 65, 67, 71, 73, 77, 79, 83, 85, 89, 91, 95, 97...]

REVEALING THE COMPOSITES IN THE PAIRSLIST

While there is no obvious pattern to the distribution of the primes (see proof why primes are not random), there is a clear pattern to the composite numbers in the list, all of the segregated pairs in the series are primes up until a². The composites in the segregated pairsList are revealed in a two step alternating pattern.

STEP ONE 

a² is the first composite in the list. from a² onwards further composites (all multiples of a) occur with the following regularity:- 

a = 5 (the first integer the pairsList) 

a² = first composite 

a² + (a x 2) = second composite 

second composite + (a x 4) = next composite

This process gets repeated by adding the alternating products of a x 2 then a x 4 to the previous composite.

This reveals the composite products of a, in the segregated pairsList:- [25, 35, 55, 65, 85, 95...]

STEP TWO 

Similar to step one only here the polarity of 2 and 4 is reversed. 

b = 7 (the second integer the pairsList) 

b² = first composite 

b² + (b x 4) = second composite 

second composite + (b x 2) = next composite

this process gets repeated by adding the alternating products of b x 4 then a x 2 to the previous composite.

This reveals the composite products of b, in the segregated pairsList:- [49, 77, 91...]

Steps one and two are repeated sequentially creating loopListOne and loopListTwo throughout the pairsList while n² < maxValue, loopListOne and loopListTwo are combined forming a compositeList and the compositeList is striped from the pairsList to form the primesList. Lastly the prime pair 2 and 3 are added to the primesList.

The illustration this demonstrates:-  It is not that primes are randomly distributed, but rather it is the composite values in the pairsList that appears random due to their incrementally increase, layering and partial overlapping. This results in an apparent random sequence. By studying how composites are distributed in pairsList we are able to reveal the pattern of the primes. 

An alternative perspective; consider the plane of natural numbers as all being potentially prime, until you add layers of multiples over it as described above, forming composite numbers in recurring patterns, but because their spacing is incrementally increased you get intermittent overlapping of composites and irregular gaps of primes forming a Jackson Pollock type canvas of composites and primes. 

NOTES

See Prime Code 02.py for an example of this written in python
Prime Code 03.py and Prime Code 04.py a variants that were used to speed up the process

The Patterns of Primes.ods spreadsheets further illustrate the the distribution of primes, with a "Prime Plain" sheet and "Pairs List & Spacing" sheet. Lastly the "Prime Factors" sheet contains a proof that illustrates, primes are not random.




