import time
import math

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
#defining variables
listOfPossibleValuesOfA = []
listOfPossibleValuesOfB = []
a = 1
b = 2
c = 3

# adding all values to the list
for i in range(1001):
    listOfPossibleValuesOfA.append(i)
    listOfPossibleValuesOfB.append(i)
print("A: ", listOfPossibleValuesOfA)
print("B: ", listOfPossibleValuesOfB)
'''
# Losing the values that aren't a Pythagorean triplet 
for i in listOfPossibleValuesOfB:
    a = listOfPossibleValuesOfA[0]
    checker = math.sqrt((a*a) + (i*i))
    if checker % 1 == 0:
        print(checker)
    else:
        print("The value for a (", a, ") and the value for b(", b, ") do not make C an integer. Therefore, making the values for a and b not applicable. ")
        listOfPossibleValuesOfB.pop(i)
        print(listOfPossibleValuesOfB)
'''
# Need to make a piece of code to square a and square b, add them together and square root it to make c.
a = 
b = 5
c = (a*a) + (b*b)
c = math.sqrt(c)
if c % 1 == 0:
    print(c)
else:
    print("C is not an integer. Therefore making the values for a and b not applicable. ")
# main part of code. Checks if all requirements fit to make the solution.
'''
if (a+b+c == 1000):
    if (a<b and b<c):
        solution = a*b*c
        print(solution)
'''
