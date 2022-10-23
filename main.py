from fastapi import FastAPI
# from database.firebase import db


app = FastAPI()


@app.get('/')
def root():
    return {
        "message": "Connected!"
    }
