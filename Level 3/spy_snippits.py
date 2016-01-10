"""
Spy snippets
============

You've been recruited by the team building Spy4Rabbits, a highly advanced search engine used to help fellow agents
discover files and intel needed to continue the operations against Dr. Boolean's evil experiments. The team is known
for recruiting only the brightest rabbit engineers, so there's no surprise they brought you on board. While you're
elbow deep in some important encryption algorithm, a high-ranking rabbit official requests a nice aesthetic feature
for the tool called "Snippet Search." While you really wanted to tell him how such a feature is a waste of time in
this intense, fast-paced spy organization, you also wouldn't mind getting kudos from a leader. How hard could it be,
anyway?

When someone makes a search, Spy4Rabbits shows the title of the page. Your commander would also like it to show a
short snippet of the page containing the terms that were searched for.

Write a function called answer(document, searchTerms) which returns the shortest snippet of the document, containing
all of the given search terms. The search terms can appear in any order.

The length of a snippet is the number of words in the snippet. For example, the length of the snippet "tastiest color
of carrot" is 4. (Who doesn't like a delicious snack!)

The document will be a string consisting only of lower-case letters [a-z] and spaces. Words in the string will be
separated by a single space. A word could appear multiple times in the document.
searchTerms will be a list of words, each word comprised only of lower-case letters [a-z]. All the search terms will
be distinct.

Search terms must match words exactly, so "hop" does not match "hopping".

Return the first sub-string if multiple sub-strings are shortest. For example, if the document is "world there hello
hello where world" and the search terms are ["hello", "world"], you must return "world there hello".

The document will be guaranteed to contain all the search terms.

The number of words in the document will be at least one, will not exceed 500, and each word will be 1 to 10 letters
long. Repeat words in the document are considered distinct for counting purposes.
The number of words in searchTerms will be at least one, will not exceed 100, and each word will not be more than 10
letters long.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) document = "many google employees can program"
    (string list) searchTerms = ["google", "program"]
Output:
    (string) "google employees can program"

Inputs:
    (string) document = "a b c d a"
    (string list) searchTerms = ["a", "c", "d"]
Output:
    (string) "c d a"
"""
def get_search_term_index_dictionary(document, searchTerms):
    # remove duplicate terms
    searchTerms = list(set(searchTerms))
    words_in_document = document.split()
    search_term_index_dictionary = {}
    for search_term in searchTerms:
        search_term_index_dictionary[search_term] = [index for index, word in enumerate(words_in_document) if
                                                     word == search_term]
    return words_in_document, search_term_index_dictionary


def find_slice_range_from_closest_matches(value, lists):
    closest_matches = [value]
    levels_deep = 0
    while levels_deep <= len(lists) - 1:
        next_match = min(lists[levels_deep], key=lambda num: abs(num - value))
        closest_matches.append(next_match)
        levels_deep += 1
    closest_matches.sort()
    return [closest_matches[0], closest_matches[len(closest_matches) - 1]]


def find_smallest_slice(index_dictionary):
    possible_slices = []
    search_term_keys = [key for key in index_dictionary]
    search_term_keys.sort(key=lambda key: len(index_dictionary[key]))
    indexes = [index_dictionary[search_term] for search_term in search_term_keys]
    for occurrence in index_dictionary[search_term_keys[0]]:
        possible_slices.append(find_slice_range_from_closest_matches(occurrence, indexes[1:]))

    # search reverse possibilities
    search_term_keys = search_term_keys[::-1]
    indexes = [index_dictionary[search_term] for search_term in search_term_keys]
    for occurrence in index_dictionary[search_term_keys[0]]:
        possible_slices.append(find_slice_range_from_closest_matches(occurrence, indexes[1:]))

    possible_slices.sort(key=lambda slice_range: (slice_range[1] - slice_range[0], slice_range[0]))

    try:
        return possible_slices[0]
    except IndexError:
        return None


def answer(document, searchTerms):
    words_in_document, search_term_index_dictionary = get_search_term_index_dictionary(document, searchTerms)
    smallest_slice = find_smallest_slice(search_term_index_dictionary)
    if smallest_slice is None:
        return None