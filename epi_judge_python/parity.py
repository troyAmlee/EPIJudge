from test_framework import generic_test

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
        # shift to the right by 1
    # otherwise: shift to the right by 1
    


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
