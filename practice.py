"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    if not words:
        return []
    else:
        uniques = set(words)
        return uniques

def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    unique1 = set(items1)
    unique2 = set(items2)
    unique_commons_count = {}
    combined_unique_commons = []

    for item1 in unique1:
        unique_commons_count[item1] = 1

    for item2 in unique2:
        unique_commons_count[item2] = unique_commons_count.get(item2, 0) + 1

    for unique_item in unique_commons_count:
        if unique_commons_count[unique_item] > 1:
            combined_unique_commons.append(unique_item)

    return combined_unique_commons



def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    pairs = {}
    uniques = list(set(numbers))
    pairs_sum_zero = []

    for num in uniques:
        for index in range(len(uniques) - 1):
            if num + uniques[index] == 0:
                 pairs[num] = uniques[index]

    temp_list = []    
    for tup in pairs.items():
        temp_flag = True
        temp_list = sorted([tup[0], tup[1]])
        for index in range(len(pairs_sum_zero)):
            if pairs_sum_zero[index] == temp_list:
                temp_flag = False
                continue
        if temp_flag:
            pairs_sum_zero.append(temp_list) 

    return pairs_sum_zero


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    char_counts = {}
    char_list = []
    count_list = []   
    no_spaces_string = phrase.replace(" ", "")
    sort_list = []

    for char in no_spaces_string:
        char_counts[char] = char_counts.get(char,0) + 1

    # sort dictionary by value. 
    for char in sorted(char_counts, key=char_counts.get):
        char_list.append(char)
        count_list.append(char_counts[char])

    if count_list[-1] == count_list[-2]:
        sort_list = sorted(char_list[-2:])
    else:
        sort_list.append(char_list[-1])

    return sort_list


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
