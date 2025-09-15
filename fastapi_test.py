from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# 환경변수에서 키 불러오기 (추천)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# 요청 스키마 정의
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 원하는 모델
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.message}
            ]
        )
        # 응답 텍스트만 꺼내서 반환
        answer = response["choices"][0]["message"]["content"]
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/get-angry-image")
async def get_angry_image():
    # 예: 추천 이미지 ID만 보내줌
    return {"image_id": "angry"}

@app.get("/get-sad-image")
async def get_sad_image():
    # 예: 추천 이미지 ID만 보내줌
    return {"image_id": "sad"}

@app.get("/get-runaway-image")
async def get_runaway_image():
    # 예: 추천 이미지 ID만 보내줌
    return {"image_id": "runaway"}