from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # pre-compute a lookup ta5ble with all reversal combinations of 16-bit integers
    mask = 2**64
    rev = '0b' + bin(x)[:1:-1]
    zeros = len(bin(mask)) - len(rev) - 1
    rev += ('0' * zeros)
    return int(rev, 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
