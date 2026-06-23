import os
from dotenv import load_dotenv
from google import genai

# 1. .env 파일에서 키 불러오기
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. 그 키로 Gemini에 연결
client = genai.Client(api_key=api_key)

# 3. 질문 하나 보내기
messages=[]
print("안녕하세요! 저는 구글 gemini-2.5-flash입니다. 궁금하신 질문을 입력해주세요! 없으시다면 공백 또는 N을 입력해주세요")
while True:
        user_input=input("질문 입력 칸:")
        is_summary=False
        if user_input=="N" or user_input=="":
            break
        elif user_input=="/초기화":
             messages.clear()
             print("기록을 지웠습니다.")
             continue
        elif user_input=="/요약":
             user_input = "지금까지의 대화를 요약해줘."
             is_summary=True
        
        try:
                 messages.append({"role": "user", "parts": [{"text": user_input}]})
                 response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=messages)
                 messages.append({"role": "model", "parts": [{"text": response.text}]})
                 print("-"*40)
                 print("-"*40)
                 print(response.text)
                 print("-"*40)
                 print("-"*40)
                 if is_summary:  #"/요약"에서 변경함.
                        messages.pop()
                        messages.pop()                      #pop()은 리스트 맨 뒤 요소를 없애는 것이기 때문에 그냥 pop()만 해도 됨!
        except:
                print("잠시 후에 다시 시도해주세요.")
                continue
