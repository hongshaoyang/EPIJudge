from collections import defaultdict
from test_framework import generic_test


def can_form_palindrome(s):
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1
    # replaceable with collections.Counter(s)

    if len(s) % 2 == 0:
        return not any(count%2==1 for count in counter.values())
    else:
        odd_flag = False
        for count in counter.values():
            if count%2==1:
                if odd_flag:
                    return False
                odd_flag = True
        return True

    # an alternative: # chars whose freqs is odd is at most 1
    # return sum(count % 2 for count in counter.values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
