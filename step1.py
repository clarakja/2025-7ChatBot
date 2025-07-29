# chatbot_step1_reset_v2.py

import streamlit as st

st.title("🧩 1단계: 조건문 챗봇")
st.write("궁금한 것을 입력해 보세요! (예: 공부, 휴식, 응원, 종료)")

# 사용자 입력 필드의 키 설정
input_key = "user_input"

# 입력값 초기화 함수 정의
def clear_input():
    st.session_state[input_key] = ""

# 입력 필드
user_input = st.text_input("너: ", key=input_key, on_change=clear_input)

# 응답 처리
if user_input:
    if "공부" in user_input:
        st.write("📘 공부는 힘들지만, 노력은 배신하지 않아!")
    elif "휴식" in user_input:
        st.write("☕ 잠깐 쉬는 것도 괜찮아. 머리를 식히자!")
    elif "응원" in user_input:
        st.write("🔥 넌 할 수 있어! 파이팅!")
    elif "종료" in user_input:
        st.write("👋 잘가! 다음에 또 이야기하자.")
    else:
        st.write("😅 미안, 그건 잘 모르겠어.")
