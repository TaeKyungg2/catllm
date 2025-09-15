from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import openai
import os
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (개발용)
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, OPTIONS 다 허용
    allow_headers=["*"],
)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# 환경변수에서 키 불러오기 (추천)


# 요청 스키마 정의
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"msg": "서버 잘 동작 중!"}

@app.post("/chat")
async def chat(request: ChatRequest):
    print(f"Received message: {request.message}")
    try:
        response =  client.chat.completions.create(
            model="gpt-3.5-turbo",  # 원하는 모델
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.message}
            ]
        )
        # 응답 텍스트만 꺼내서 반환
        answer = response.choices[0].message.content
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/get-angry-image")
async def get_angry_image():
    # 예: 추천 이미지 ID만 보내줌
    return {"image_id": "angry.gif"}

@app.get("/get-sad-image")
async def get_sad_image():
    # 예: 추천 이미지 ID만 보내줌
    return {"image_id": "sad"}

@app.get("/get-runaway-image")
async def get_runaway_image():
    # 예: 추천 이미지 ID만 보내줌
    return {"image_id": "runaway"}

