from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/reverse_integers")
def reverse_integers(integer: str):
    if integer[0] == '-':
        minus = integer[0]
        num_reversed = integer[::-1][:-1]
        return {"result": f"{minus}{num_reversed}"}
    
    return {"result": integer[::-1]}

@app.get("/average_words_length")
def get_average_words_length(sentence: str):
    regex = r'\W+' # expressao regular que identifica somente letras, tudo o que nao for letra é descartado
    words_list = list(filter(None, re.split(regex, sentence))) # filtrando todas as palavras da lista, para eliminar strings vazias que foram retornadas em re.split()
    
    total_words = 0
    total_words_length = 0

    for word in words_list:
        total_words_length += len(word)
        total_words += 1

    return round(total_words_length/total_words, 2)

@app.get("/matched_mismatched_words")
def matched_mismatched_words(sentence1: str, sentence2: str):
    regex = r'\W+'
    words_list = list(filter(None, re.split(regex, sentence1))) # todas as palavras da frase sao armazenadas na variavel em forma de lista
    words_list2 = list(filter(None, re.split(regex, sentence2)))# as duas listas serao iteradas para verificar as palavras em comum
    matched_words= set()
    mismatched_words = set()

    for word in words_list:
        if word in words_list2:
            matched_words.add(word)
        else:
            mismatched_words.add(word)

    for word in words_list2:
        if word not in words_list:
            mismatched_words.add(word)
    
    return [mismatched_words, matched_words]
