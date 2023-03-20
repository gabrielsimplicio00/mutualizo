from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import re
import sys
sys.path.append('./src')
from users import *

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

def generate_fake_hash_password(password: str):
    return "fakehashed" + password

@app.post("/auth")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username) # os dados do campo username vão servir para buscar o usuário no banco de dados fake

    if not user_dict: # se o usuário não existir no banco uma exceção é lançada
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserInDB(**user_dict)
    hashed_password = generate_fake_hash_password(form_data.password) # a partir da senha digitada, uma fake hash é criada

    if not hashed_password == user.hashed_password: # se a senha com hash não for igual a que está armazenada no banco uma exceção é lançada
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    if user.disabled == True: # se o usuário estiver desabilitado uma exceção é lançada
        raise HTTPException(status_code=403, detail="Credentials not allowed")

    return {"access_token": user.username, "token_type": "bearer"}

def generate_words_list(sentence): # D.R.Y, essa lógica se repetia na aplicação
    regex = r'\W+' # expressao regular que identifica somente letras e descarta o que não for
    words_list = list(filter(None, re.split(regex, sentence))) # o filter() elimina strings vazias que foram retornadas em re.split()
    return words_list

@app.get("/")
def index():
    return {"rota para a testagem de endpoints":
        "http://localhost:8000/docs"
    }

@app.get("/reverse_integers")
def get_reverse_integers(integer: int, token: str = Depends(oauth2_scheme)):
    integer = str(integer) # tipar a variavel para que só sejam aceitos números inteiros, depois fazer o casting para str e iterar

    if integer[0] == '-':
        minus = integer[0] # se o numero for negativo, o sinal de menos é armazenado para ser usado posteriormente
        num_reversed = integer[::-1][:-1] # [::-1] retorna os itens de maneira invertida, [:-1] retira o ultimo elemento (que nesse caso é o sinal -)
        return {"resultado": f"{minus}{num_reversed}"}
    
    return {"resultado": integer[::-1]}

@app.get("/average_words_length")
def get_average_words_length(sentence: str, token: str = Depends(oauth2_scheme)):
    words_list = generate_words_list(sentence)

    total_words = 0
    total_words_length = 0

    for word in words_list:
        total_words_length += len(word)
        total_words += 1

    return {"resultado": round(total_words_length/total_words, 2)}

@app.get("/matched_mismatched_words")
def get_matched_and_mismatched_words(sentence1: str, sentence2: str, token: str = Depends(oauth2_scheme)):
    words_list1 = generate_words_list(sentence1) # todas as palavras da frase sao armazenadas na variavel em forma de lista
    words_list2 = generate_words_list(sentence2) # as duas listas serao iteradas para verificar as palavras em comum
    
    matched_words= set()
    mismatched_words = set()

    for word in words_list1:
        if word in words_list2:
            matched_words.add(word)
        else:
            mismatched_words.add(word)

    for word in words_list2:
        if word not in words_list1:
            mismatched_words.add(word)

    return {"resultado": [mismatched_words, matched_words]}
