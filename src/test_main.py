from main import *

def teste_reverse_integers():
    assert reverse_integers("-123") == {"result": "-321"}

def teste_average_words_length():
    sentence = 'Hi all, my name is Tom...I am originally from Brazil.'
    assert get_average_words_length(sentence) == 3.55

def teste_matched_mismatched_words():
    sentence1 = "We are really pleased to meet you in our city"
    sentence2 = "The city was hit by a really heavy storm"
    result = [{'We', 'to', 'heavy', 'The', 'storm', 'meet', 'hit', 'pleased', 'are', 'by', 'a', 'in', 'was', 'you', 'our'}, {'really', 'city'}]
    assert matched_mismatched_words(sentence1, sentence2) == result

def teste_login(): #?
    pass