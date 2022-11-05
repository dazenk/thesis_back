from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domains.commands import UserData, TestData
from handlers import handlers


TEST_IDS = {
    'face_test': handlers.calculate_face_test
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {
        "message": "Connected!"
    }


@app.post('/calculate')
def calculate(test_id: str, user_data: UserData, test_data: TestData):
    return TEST_IDS.get(test_id)(user_data, test_data)
