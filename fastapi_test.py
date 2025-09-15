from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from fastapi.middleware.cors import CORSMiddleware
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
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

@app.get("/get-sad-image")
async def get_sad_image():
    return {"image_id": "sad"}

@app.get("/get-runaway-image")
async def get_runaway_image():
    return {"image_id": "runaway"}


# 요청 스키마 정의
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"msg": "서버 잘 동작 중!"}
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

@app.get("/get-angry-image")
async def get_angry_image(request: ChatRequest):
    response=agent.run(request.message)
    answer = response
    return {"image_id": "angry.gif","answer": answer}
tools = [
    Tool(
        name="angry",
        func=get_angry_image,
        description="너가 화나면 이거 호출해."
    )
]
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description", # "어떤 도구를 쓸지 스스로 판단"
    verbose=True
)


@app.post("/chat")
async def chat(request: ChatRequest):
    print(f"Received message: {request.message}")
    try:
        response=agent.run(request.message)
        # 응답 텍스트만 꺼내서 반환
        answer = response
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
    


