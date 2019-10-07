from collections import defaultdict
from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    sorted_string_to_anagrams = defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
        (k, group) for k, group in sorted_string_to_anagrams.items()
        if len(group) >= 2
    ]


res = find_anagrams(("debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money"))
print(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
