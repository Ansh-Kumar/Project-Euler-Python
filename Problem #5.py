# Problem: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?
import time
'''
Algorithms to Solve Euler #5


'''

i = 20
startTime = time.time()
while (i % 11 != 0 or i % 12 != 0 or i % 13 != 0 or i % 14 != 0 or i % 15 != 0 or i % 16 != 0 or i % 17 != 0 or i % 18 != 0 or i % 19 != 0 or i % 20 != 0):
    i += 20
    if (i%200000 == 0):
        print(i)
elapsedTime = round(time.time() - startTime)
print ("The Smallest Number Is", i, "in", elapsedTime, "Seconds")
print(232792560)
