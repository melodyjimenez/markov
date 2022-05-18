"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path_1, file_path_2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents_1 = open(file_path_1).read()
    contents_2 = open(file_path_2).read()
    
    return contents_1 + contents_2


def make_chains(text_string, n_grams):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    for i in range(len(words) - n_grams):
        words_gram_list = words[i: i + n_grams]
        words_gram = tuple(words_gram_list)
    
        if words_gram not in chains.keys():
            chains[words_gram] = [words[i+n_grams]]
        else:
            chains[words_gram].append(words[i+n_grams])
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    
    # your code goes here
    first_word_list = []
    end_punc = []
    for word_keys in chains:
        if word_keys[0][0].isupper():
            first_word_list.append(word_keys)
    for word_keys in chains:
        if word_keys[-1][-1] in [".", "!", "?"]:
            end_punc.append(word_keys)



    # random_key = choice(list(chains))
    # words.extend(list(random_key))

    random_key = choice(first_word_list)
    words.extend(list(random_key))

    
    # while random_key in chains:
    while random_key not in end_punc:
        next_word = choice(chains[random_key])
        words.append(next_word)
        random_key_list = list(random_key)
        random_key_list.pop(0)
        random_key_list.append(next_word)
        random_key = tuple(random_key_list)

    return ' '.join(words)


input_path_1 = sys.argv[1]
input_path_2 = sys.argv[2]
n = int(sys.argv[3])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path_1, input_path_2)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains)
# print (chains)
print(random_text)

