# jaccard.py: Computes the similarity between two files using the jaccard index
# See: https://en.wikipedia.org/wiki/Jaccard_index

import sys
import string

def read_words_from_file(file):
    """
    Opens a file and returns all the words contained in the file.
    The words are converted using the clean function.
    """
    data = file.read()
    list_of_words = []
    for word in data.split(' '):
        clean_word = clean(word)
        list_of_words.append(clean_word)
    return list_of_words

def clean(word):
    """
    Cleans a word: remove punctuation and whitespace and convert to
    lower case.
    """
    return word.lower().strip(string.punctuation + string.whitespace)

# Optimize this function.
# Complexity before optimization: ?
# Complexity after optimization: ?
def unique_items(collection):
    """
    Removes duplicate elements from the collection.
    """
    unique = []
    for element in collection:
        if element not in unique:
            unique.append(element)
    return unique

# Optimize this function.
# Complexity before optimization: ?
# Complexity after optimization: ?
def intersection(collection1, collection2):
    """
    Return the intersection of the two collections
    (all the elements that are in both collections).
    """
    intersection_list = []
    for element in collection1:
        if element in collection2:
            intersection_list.append(element)
    return intersection_list

# Optimize this function.
# Complexity before optimization: ?
# Complexity after optimization: ?
def union(collection1, collection2):
    """
    Return the union of the two collections
    (all the elements that are in at least one of the collections).
    """
    return unique_items(collection1 + collection2)


# Complexity before optimization: ?
# Complexity after optimization: ?
def main():
    # Check command line args
    if len(sys.argv) < 3:
        sys.exit(f'Usage python {sys.argv[0]} file1 file2')

    # Open both text files and convert to list of words
    with open(sys.argv[1], 'r', encoding = 'ISO-8859-1') as file1:
        words1 = read_words_from_file(file1)

    with open(sys.argv[2], 'r', encoding = 'ISO-8859-1') as file2:
        words2 = read_words_from_file(file2)

    # Convert words collection to bags of words
    bag_of_words1 = unique_items(words1)
    bag_of_words2 = unique_items(words2)

    # Compute jaccard score
    intersection_bag = intersection(bag_of_words1, bag_of_words2)
    union_bag = union(bag_of_words1, bag_of_words2)
    jaccard_index = len(intersection_bag) / len(union_bag)

    print(f'Jaccard index of {sys.argv[1]} and {sys.argv[2]}: {jaccard_index:.3f}')

main()
