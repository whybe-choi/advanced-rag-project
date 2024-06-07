import streamlit as st

def init_streamlit():
    st.set_page_config(page_title="Dr.KHU🥼", page_icon="🩺")

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요! Dr.KHU🥼입니다 😊"}]

    for messages in st.session_state.messages:
        with st.chat_message(messages["role"]):
            st.write(messages["content"])

if __name__ == "__main__":
    init_streamlit()