from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def pong():
    return {"ping": "pong!"}