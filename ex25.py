def break_words(stuff):
    """This funtion will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_words(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentance(sentance):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentance)
    return sort_words(words)

def print_first_and_last_sentance(sentance):
    """Prints the first and the last words of the sentence."""
    words = break_words(sentance)
    print_first_words(words)
    print_last_word(words)

#To use this example type python3.8 in terminal to get >>>
# import ex25 (no need to type ex25.py)
# sentence = "All good things come to those who wait."
# words = ex25.break_words(sentence)
# words
# sorted_words = ex25.sort_words(words)
