from main import *

def teste_reverse_integers():
    assert reverse_integers("-123") == {"result": "-321"}

def teste_average_words_length():
    sentence = 'Hi all, my name is Tom...I am originally from Brazil.'
    assert get_average_words_length(sentence) == 3.55