import streamlit as st

st.title("🧩 1단계: 조건문 챗봇")

input_key = "user_input"
response_key = "bot_response"

# 입력 필드
user_input = st.text_input("너: ", key=input_key)

# 챗봇 응답 처리
if user_input:
    if "공부" in user_input:
        st.session_state[response_key] = "📘 공부는 힘들지만, 노력은 배신하지 않아!"
    elif "휴식" in user_input:
        st.session_state[response_key] = "☕ 잠깐 쉬는 것도 괜찮아. 머리를 식히자!"
    elif "응원" in user_input:
        st.session_state[response_key] = "🔥 넌 할 수 있어! 파이팅!"
    elif "종료" in user_input:
        st.session_state[response_key] = "👋 잘가! 다음에 또 이야기하자."
    else:
        st.session_state[response_key] = "😅 미안, 그건 잘 모르겠어."

    # 입력값 초기화
    st.session_state[input_key] = ""

# 응답 출력
if response_key in st.session_state:
    st.write("🤖 챗봇:", st.session_state[response_key])
