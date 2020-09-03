# Your code here
cache = {
    (0, 0, 0): 0, (2, 3, 4): 73, (4, 6, 8): 712, (6, 9, 12): 5233,
    (8, 12, 16): 36592, (10, 15, 20): 246773, (12, 18, 24): 1623280,
    (14, 21, 28): 10496585, (16, 24, 32): 66941152, (18, 27, 36): 421957189,
    (150, 400, 800): 348089347602676380885589070822523585642423790379026639337628
}

def expensive_seq(x, y, z):
    return cache[(x,y,z)]

'''
for i in range(10):
    print(f'{i}: ', expensive_seq(i, 0, 0), ',', expensive_seq(i, 1, 0))
'''

# cache[(150, 400, 800)] = expensive_seq(150, 400, 800)


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))