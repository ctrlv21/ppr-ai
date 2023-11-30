import streamlit as st
import utils
st.title('ppr.ai')
st.subheader('Exam Prep Assistant using LLMs')

with st.sidebar:
        st.sidebar.header("Your pdfs")
        st.write('Please enter your name')
        name = st.text_input('Name')
        pdf_files = st.file_uploader("Choose files", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                # get pdf files
                raw_text = utils.read_files(pdf_files)
                print(raw_text)    
                # split text into chunks
                # text_chunks = get_chunks(raw_text)
                # store chunks in vectorstore
                # vectorstore = get_vectorstore(text_chunks)
                # create conversation chain
                # st.session_state.conversation = get_conversation_chain(vectorstore)
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
                response = "This is a test response"
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)
        
with open( "./style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
