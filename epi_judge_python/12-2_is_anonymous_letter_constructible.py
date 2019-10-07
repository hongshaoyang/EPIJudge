from collections import defaultdict
from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # compute freqs
    count = defaultdict(int)
    for char in magazine_text:
        count[char] += 1
    for char in letter_text:
        count[char] -= 1
    # if any of the freqs are -ve, the letter cannot be written
    cannot_be_written = any(v < 0 for v in count.values())
    return not cannot_be_written




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
