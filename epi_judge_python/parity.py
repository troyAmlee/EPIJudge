from test_framework import generic_test

<<<<<<< HEAD
cache = {}
def parity(x: int) -> int:
    count = 0

    while x:
        if(x in cache):
            return cache[x]
        if(x & 1):
            count += 1
            x >>= 1
        else:
            x >>= 1
    count = (count & 1)
    cache[x] = count
    return count
    # 10011001
    # check lowermost bit if it is a one
    # count it
    # otherwise: shift to the right by 1
    
=======
# How would you compute the parity of a very large number of 64 bit words?
# Odd number of ones '1101 == 1'
# Even number of ones '100001000 == 0'
d = {}
def parity(x: int) -> int:
    summ = 0
    conv = bin(x)
    stringify = str(conv)
    listify = list(stringify)
    if(x not in d):
        
        for i in listify:
            if(i == "1"):
                summ += 1
        if(summ % 2 == 0):
            d[x] = 0
            return 0
        elif(summ % 2 == 1):
            d[x] = 1
            return 1
    else:
        print("---CACHE ACCESSED---")
        return d[x]

>>>>>>> dc2e73235480a77fc25edf52684487bfbd838cd0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
