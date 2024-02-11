import streamlit as st
import utils
st.title('ppr.ai')
st.subheader('Exam Prep Assistant using LLMs')

with st.sidebar:
        st.sidebar.header("Your files")
        st.write('Please enter your name')
        name = st.text_input('Name')
        files = st.file_uploader("Choose files", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                utils.process_files(files)
                st.success("Done!")
                st.snow()

if name:
    if ("messages" not in st.session_state.keys()):
        st.session_state.messages = [{"role": "assistant", "content": f"Hello! {name}, Welcome to ppr.ai. How can I help you?"}]

    for message in st.session_state.messages:
        if(message["role"] == "assistant"):
            with st.chat_message(message["role"],avatar="✨"):
                st.write(message["content"])
        else:
            with st.chat_message(message["role"],avatar="🙋‍♂️"):
                st.write(message["content"])

    if prompt := st.chat_input(disabled=not (name)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user",avatar="🙋‍♂️"):
            st.write(prompt)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant",avatar="✨"):
            with st.spinner():
                # response = chatbot_utils.reply(name,prompt,code)
                response = utils.answer_question(name,prompt)
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)
        
with open( "./style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
