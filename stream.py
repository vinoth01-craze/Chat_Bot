import streamlit as st

def simple_chatbot(user_input):
    user_input = user_input.lower()
    if 'name' in  user_input:
        return 'your name is VINOTH'
    elif 'hello' in user_input:
        return 'hello i am chatbot how can i help you'
    elif 'age' in user_input:
        return 'your age is 19..'
    elif 'college' in user_input:
        return 'you are currently doing in NANDHA ENGINEERING COLLEGE'
    elif 'bye' in user_input:
        return 'bye have a nice day to you..'
    else:
        return 'I am a simple chatbot and can respond to basic greetings.'


st.title("Simple Chatbot with Streamlit")

user_input = st.text_input("You: ", "")
if user_input:
    response = simple_chatbot(user_input)
    if st.button("Send "):
        st.text_area("Bot:", value=response, height=100)
