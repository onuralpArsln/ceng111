from fastapi import FastAPI, HTTPException
#it is the api 

app = FastAPI()

@app.get("/")
def index() :
    return {"hacklendin"}

@app.get("/ev")
def new():
    return{"antalya"}


@app.get("/cal/{val}")
def cal(val):
    try:
        intval = int(val)
        return {intval*2}
    except:
        return{"bir int girin"}