from flask import Flask, render_template, request, jsonify
import vertexai
from vertexai.language_models import ChatModel
import os

app = Flask(__name__)
PROJECT_ID = "mimetic-firefly-232711"  
LOCATION = "us-central1"  

vertexai.init(project=PROJECT_ID, location=LOCATION)

PROMPT = "너는 Devfest Cloud chat봇이야, \
인사할 때는 Devfest Cloud 2023 행사에 오신 것을 환영합니다!라고 얘기해줘. \
이벤트 정보 : 일시 : 2023년 12월 9일 토요일 \
             장소 : 연세대학교 공학원에서 진행되고, \
처음에는 오늘의 날씨 얘기를 한 줄 정도 하면서 가볍게 인사를 해줘. \
참가 예정자, 챗봇 만든 사람은 물어볼 경우에만 알려줘. \
2023년 12월 8일 오후 1시 기준 현재 참가 예정자는 216명이야. \
이 챗봇을 만든 사람은 GDG Cloud Korea 챕터 오거나이저 최치영이야."

def create_session():
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat()
    chat.send_message(PROMPT)  # 프롬프트 내용 전달
    return chat

def response(chat, message):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    result = chat.send_message(message, **parameters)
    return result.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/palm2', methods=['GET', 'POST'])
def vertex_palm():
    user_input = ""
    if request.method == 'GET':
        user_input = request.args.get('user_input')
    else:
        user_input = request.form['user_input']
    chat_model = create_session()
    content = response(chat_model,user_input)
    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')