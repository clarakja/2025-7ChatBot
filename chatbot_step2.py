# chatbot_step2_fixed.py

import streamlit as st

st.title("🧠 2단계: 기억하는 챗봇")

# 세션 상태 초기화
if "name" not in st.session_state:
    st.session_state.name = ""
if "mood" not in st.session_state:
    st.session_state.mood = ""
if "response" not in st.session_state:
    st.session_state.response = ""
if "name_input" not in st.session_state:
    st.session_state.name_input = ""
if "mood_input" not in st.session_state:
    st.session_state.mood_input = ""

# 이름 입력 단계
def save_name():
    st.session_state.name = st.session_state.name_input

if not st.session_state.name:
    st.text_input("이름을 알려줘!", key="name_input", on_change=save_name)
    st.stop()

# 기분 입력 단계
def save_mood():
    st.session_state.mood = st.session_state.mood_input

if not st.session_state.mood:
    st.text_input("지금 기분은 어때?", key="mood_input", on_change=save_mood)
    st.stop()

# 대화 입력창
user_input = st.text_input("너: ", key="user_input")

# 응답 처리
if user_input:
    name = st.session_state.name
    mood = st.session_state.mood

    if "공부" in user_input:
        st.session_state.response = f"📘 {name}, 오늘도 열공 중이구나! {mood}한 기분이지만 잘하고 있어!"
    elif "휴식" in user_input:
        st.session_state.response = f"☕ {name}, {mood}할 땐 잠깐 쉬는 것도 좋아!"
    elif "응원" in user_input:
        st.session_state.response = f"🔥 {name}, 넌 정말 잘하고 있어! 계속 힘내자!"
    elif "종료" in user_input:
        st.session_state.response = f"👋 안녕 {name}, 다음에 또 보자!"
    else:
        st.session_state.response = f"😅 미안해 {name}, 그건 잘 모르겠어."

    st.session_state.user_input = ""

# 응답 출력
if st.session_state.response:
    st.write("🤖 챗봇:", st.session_state.response)
