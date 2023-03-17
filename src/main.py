from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import bcrypt
import re

fake_users_db = {
    "userteste": {
        "username": "userteste",
        "full_name": "Teste",
        "email": "teste@email.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    }
}

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # password flow (OAuth2)

class User(BaseModel):
    username: str
    email:str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def generate_fake_hash_password(password: str):
    salt = bcrypt.gensalt() # ainda vou pensar em como implementar
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return "fakehashed" + password

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = generate_fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/reverse_integers")
def reverse_integers(integer: str, token: str = Depends(oauth2_scheme)):
    if integer[0] == '-':
        minus = integer[0]
        num_reversed = integer[::-1][:-1]
        return {"result": f"{minus}{num_reversed}"}
    
    return {"result": integer[::-1]}

@app.get("/average_words_length")
def get_average_words_length(sentence: str, token: str = Depends(oauth2_scheme)):
    regex = r'\W+' # expressao regular que identifica somente letras, tudo o que nao for letra é descartado
    words_list = list(filter(None, re.split(regex, sentence))) # filtrando todas as palavras da lista, para eliminar strings vazias que foram retornadas em re.split()
    
    total_words = 0
    total_words_length = 0

    for word in words_list:
        total_words_length += len(word)
        total_words += 1

    return round(total_words_length/total_words, 2)

@app.get("/matched_mismatched_words")
def matched_mismatched_words(sentence1: str, sentence2: str, token: str = Depends(oauth2_scheme)):
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
