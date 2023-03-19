from main import *

def teste_reverse_integers():
    number = "-123"
    result = "-321"
    assert get_reverse_integers(number) == {"resultado": result}

def teste_average_words_length():
    sentence = 'Hi all, my name is Tom...I am originally from Brazil.'
    result = 3.55
    assert get_average_words_length(sentence) == {"resultado": result}

def teste_matched_mismatched_words():
    sentence1 = "We are really pleased to meet you in our city"
    sentence2 = "The city was hit by a really heavy storm"
    result = [{'We', 'to', 'heavy', 'The', 'storm', 'meet', 'hit', 'pleased', 'are', 'by', 'a', 'in', 'was', 'you', 'our'}, {'really', 'city'}]
    assert get_matched_and_mismatched_words(sentence1, sentence2) == {"resultado": result}
