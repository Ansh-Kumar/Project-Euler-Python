import math
import time


'''
### Problem 1

list = []
for x in range(1000):
  if(x % 3 == 0):
    list.append(x)
  elif(x%5 == 0):
    list.append(x)
a = sum(list)
print(a)
'''

### Problem 5

i = 2050
startTime = time.time()
'''
while (i != 2 or i != 3 or i != 5 or i != 7 or i % 11 != 0  or i % 13 != 0 or i % 17 != 0 or i % 19 != 0):
    i += 20
    print (i)
'''
elapsedTime = round(time.time() - startTime)
print ("The Smallest Number Is", i, "in", elapsedTime, "Seconds")
print(232792560)
print ((2^4)*(3^3)*(5*7(11*13*17*19))

'''
### Problem 9


listOfPossibleValuesOfA = []
listOfPossibleValuesOfB = []
a = 1
b = 2
c = 3

for i in range(0)
    listOfPossibleValuesOfA.append(i)
    listOfPossibleValuesOfB.append(i)
print("A: ", listOfPossibleValuesOfA)
print("B: ", listOfPossibleValuesOfB)


a = 1
b = 5
c = (a*a) + (b*b)
c = math.sqrt(c)
if c % 1 == 0:
    print(c)
else:
    print("C is not an integer. Therefore making the values for a and b not applicable. ")

if (a+b+c == 1000):
    if (a<b and b<c):
        solution = a*b*c
        print(solution)

### Problem 6
tot1 = 0
tot2 = 0
diff = 0
blank = []
for i in range(1,101):
  blank.append(i)



def sum_of_squares():
  global tot1
  for i in range(len(blank)):
    tot1 += blank[i]*blank[i]
  return tot1




def square_of_squares():
  global tot2
  tot2 = sum(blank) * sum(blank)
  return tot2


def difference():
  global diff
  diff = square_of_squares() - sum_of_squares()
  print(diff)
difference()


###Problem 10


sum = 0
list_for_simple = [2]
for i in range(2, 10):
  if i % 2 != 0:
    list_for_simple.append(i)
list_for_simple = sorted(list_for_simple)
print (list_for_simple)

for number in list_for_simple:
    prime = True
    for x in range(2, number):
        if number % x == 0:
            prime = False
    if prime:
        sum += number

print ("Sum =", sum)
'''
