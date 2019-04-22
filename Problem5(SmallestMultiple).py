import math
import time
start = time.time()
def isDivisible():
    n = 0
    random = True
    while random:
        n += 1
        for i in range(1, 11):
            if n % 2 != 0:
                break
            if n % 3 != 0:
                break
            if n % 5 != 0:
                break
            if n%i != 0:
                break
            if i == 20:
                random = False
            if n % 1000000 == 0:
                print(n)
    end = time.time() - start
    print(n)
    print(end)
isDivisible()
