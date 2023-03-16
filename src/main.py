from fastapi import FastAPI

app = FastAPI()

@app.get("/reverse_integers")
def reverse_integers(integer: str):
    if integer[0] == '-':
        minus = integer[0]
        num_reversed = integer[::-1][:-1]
        return {"result": f"{minus}{num_reversed}"}
    
    return {"result": integer[::-1]}
