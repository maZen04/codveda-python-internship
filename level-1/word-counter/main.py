import pprint
import string

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("The file name or directory is wrong.")
        return None

def cleaning(text):
    cleaned_text = text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    return cleaned_text.lower()


def text_to_words(text):
    words = text.split()
    return words

def word_counter(words):
    words_counter = {}
    for word in words:
        if word in words_counter:
            words_counter[word] += 1
        else:
            words_counter[word] = 1
    
    return words_counter


content = read_file('word-counter/empty.txt')

if content is not None:
    cleaned_text = cleaning(content)
    words = text_to_words(cleaned_text)
    word_counts = word_counter(words)
    pprint.pprint(word_counts)
