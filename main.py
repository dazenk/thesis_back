from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from domains.commands import UserData, FaceTestData, SpanTestData
from handlers import handlers


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


@app.post('/calculate_face_test')
def calculate_face_test(user_data: UserData, test_data: FaceTestData):
    return handlers.calculate_face_test(user_data, test_data)


@app.post('/calculate_span_test')
def calculate_span_test(user_data: UserData, test_data: SpanTestData):
    return handlers.calculate_span_test(user_data, test_data)
