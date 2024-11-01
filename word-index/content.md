# Indexing words
For this assignment you will build an indexing system for the same books as use in the previous assignments.

The goal is to be able to search a word in a given text. The program should show all lines where this word occurs.

## Example

For example, if we want to find the word "dinner" in the collected works of Jane Austen:

    $ python word_index.py texts/austen.txt
    Index built for texts/austen.txt. Type the word you want to look up.

    Enter search term: dinner

    The word "dinner" can be found on lines: 258, 289, 1096, 1166, 1186, 1885, 2142, 2302, 2307, 2321, 3598, 4187, 4261, 4871, 5031, 5344, 5449, 5463, 5524, 5698, 7073, 7412, 8709, 9406, 9513, 10484, 11246, 11320, 11401, 11538, 11654, 11770, 12816
    ...

*Note that although the example above prints the lines in ascending order, your code doesn't have to do this.*

## Get started

* Download the provided code here: [download word_index.zip](word_index.zip).
* Unzip the files into the same working directory as the Jaccard assignment (e.g. `complexity`).

In this zip you'll find two files:

- `word_index.py`: This file already contains quite a bit of starting code. You will have to fill in the missing pieces.
- `stopwords.txt`: This file contains a list of words that can be ignored by the indexing system. (So, we don't have to index a gazillion occurrences of, for example, the word "the".)

## Functions:

The code contains several predefined functions. Some of them are not finished yet and are up to you to complete.

* `read_stopwords()`: This function is partly implemented, but should be finished by you. Read all the stop words from the file "stopwords.txt" and returns a collection of those stop words.

* `convert_word()`: This function is already implemented for you. It strips a word from all punctuation, whitespace, and digits. And it converts the word to lowercase.

* `create_index()`: This function should be implemented by you. It creates an index for all words in the input file.

    * For each word in the file, the index should contain a record of all line numbers where this word occurs.
    * The type of data structure you plan to use for this index is up to you. But you have to make sure that the function `search_index()` can use it to find the line numbers of a given word.
    * Words should be cleaned by `convert_words()`
    * Empty strings and stop words should not be indexed.

* `search_index()`: This function should be implemented by you. Search the index on a specific word. Returns all the lines where the word occurs.

    * The functions `create_index()` and `search_index()` depend on each other. So, whatever data structure you chose as index in the first function (`book_index = create_index(sys.argv[1], stopwords)`) will be used by the second function to find all the line numbers (`line_numbers = search_index(searched_word, book_index)`.

* `show_search_results()`: This function should be implemented by you. Neatly print the search results.

* `user_input_search()`: This function is already implemented for you. This takes care of the user interaction. It repeatedly asks the user for a word and calls `search_index()` to find it. This function stops as soon as the user enters an empty string or the text "q", "Q", or "quit"


### Goal

Implement the missing parts of the functions above.

### Testing your program

Test your code by running it on the example at the top of the page.

Try some examples for yourself.

What happens if you search a word that does not appear in the text?

What happens if you search the word "the"?

# Complexity questions, part 3

In the file `questions.txt` that you created earlier, write down the answers to the questions below.

### Question 11

Consider the total number of words from the book included in the index to be
the input size **N** for the `search_index()` function.

What is the complexity of using your `search_index()` function to search for a
single word in the index? Explain your answer.

### Question 12

What is the complexity of the function `create_index()`? Explain your answer.
