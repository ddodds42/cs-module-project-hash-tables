import time
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    funs = {
        (2, 3): 8064, (3, 3): 575429758, (4, 3): 23014247, (5, 3): 179017319,
        (6, 3): 959638969, (7, 3): 281170720, (8, 3): 156534393,
        (9, 3): 412684903, (10, 3): 848369989, (11, 3): 246727355,
        (12, 3): 203572110, (13, 3): 183969241, (2, 4): 410731503,
        (3, 4): 764750756, (4, 4): 237974173, (5, 4): 624454993,
        (6, 4): 238640537, (7, 4): 528308127, (8, 4): 211470843,
        (9, 4): 738371044, (10, 4): 226457743, (11, 4): 511248842,
        (12, 4): 842313213, (13, 4): 598075902, (2, 5): 631239195,
        (3, 5): 651679062, (4, 5): 12615158, (5, 5): 917230692,
        (6, 5): 486616558, (7, 5): 141814354, (8, 5): 458761369,
        (9, 5): 467423111, (10, 5): 706250865, (11, 5): 295851935,
        (12, 5): 840852698, (13, 5): 381057234
}
    return funs[(x,y)]

start = time.time()

'''
THIS CODE CREATED THE CACHE!
bigs = []
y = 5
for i in range(2, 14):
    x = slowfun_too_slow(i,y)
    print('{:,}'.format(x))
    funs[(i,y)] = x

print()
print(funs, '\n')

print(f'{time.time()-start} seconds')
'''


# print(len(facts)==q)
# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
print(f'{time.time()-start} seconds')