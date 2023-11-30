import streamlit as st
st.title('ppr.ai')
st.subheader('Exam Prep Assistant using LLMs')

with st.sidebar:
    st.write('Please enter your name')
    name = st.text_input('Name')

if name:
    if ("messages" not in st.session_state.keys()):
        st.session_state.messages = [{"role": "mrppr", "content": f"Hello! {name}, Welcome to ppr.ai. How can I help you?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input(disabled=not (name)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    if st.session_state.messages[-1]["role"] != "mrppr":
        with st.chat_message("mrppr"):
            with st.spinner():
                # response = chatbot_utils.reply(name,prompt,code)
                response = "This is a test response"
                st.write(response) 
        message = {"role": "mrppr", "content": response}
        st.session_state.messages.append(message)