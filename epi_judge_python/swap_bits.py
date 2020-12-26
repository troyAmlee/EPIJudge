from test_framework import generic_test


def swap_bits(x, i, j):
    if((x >> i) & 1 == (x >> j) & 1):
        return x

    print(f"i extraction {(x >> i) & 1}")
    print(f"j extraction {(x >> j) & 1}")

    if(i == 0):
        mask1 = 1
    else:
        mask1 = 1 << i
    if(j == 0):
        mask2 = 1
    else:
        mask2 = 1 << j

    x ^= mask1

    x ^= mask2

    return x
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
