import os
from dotenv import load_dotenv
from google import genai

# 1. .env 파일에서 키 불러오기
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. 그 키로 Gemini에 연결
client = genai.Client(api_key=api_key)

# 3. 질문 하나 보내기
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="양자역학이 무슨 학문인지 한 문장으로 설명해줘."
)

# 4. 답을 화면에 출력
print(response.text)
