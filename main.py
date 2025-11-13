
from fastapi import FastAPI
import uvicorn

app = FastAPI()



@app.get("/test")
async def testing():
    return {"msg" : "hi from test"}
    
@app.get("/test/{name}")
async def test(name: str):
    return load_data(name) 
    
@app.post("/caesar")
def caesar(string: str, k: int, mode):
    encrypted = caesar_encrypt(string, k)
    decrypt = caesar_decryp(string, k)  
    if mode == "encrypt":  
        return { "encrypted_text": encrypted }
    elif mode == "decrypt":
        return {"decrypted_text": decrypt}

@app.get("/fence/encrypt")
def rail_encrypt(text: str):
    rail_text = rail_action_en(text)
    return { "encrypted_text": rail_text }

@app.post("/fence/decrypt")
def rail_decrypt(text: str):
    rail_text_de = rail_action_de(text)
    return {"decrypted": rail_text_de}


file_txt = "name.txt"

def load_data(name):
    with open(file_txt, "a") as f:
        return f.write(name) 
          
list_abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def caesar_encrypt(string: str, k: int):
    st = string.replace(" ", "")
    word1 = ""
    for i in st:
        index = list_abc.index(i) +k
        word1 += list_abc[index % 26]
    return word1
      
  
def caesar_decryp(string: str, k: int):
    st = string.replace(" ", "")
    word1 = ""
    for i in st:
        index = list_abc.index(i) -k
        word1 += list_abc[index % 26]
    return word1
  
def rail_action_en(text: str):
    txt = text.replace(" ", "")
    word_even = ""
    word_odd = ""
    for i in txt:
        index = list_abc.index(i)
        if index % 2 == 0:
            word_even += list_abc[index]
        else:
            word_odd += list_abc[index]
    return word_even + word_odd


def rail_action_de(text: str):
    txt = text.replace(" ", "")
    word2 = ""
    for i in txt:
        index = list_abc.index(i)
        if index % 2 == 0:
            word2 += list_abc[index]
        else:
            word2 += list_abc[index]
    return word2


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)