import streamlit as st

def simple_chatbot(user_input):
    user_input = user_input.lower()
    if 'my name' in user_input:
        return 'your name is VARUNA)'
    elif 'brother' in user_input:
        return ('your brother name is DIVID ...\n its amazing it is a palindrom letter right...')
    else:
        return 'I am a simple chatbot and can respond to basic greetings.'

def main():
    st.title("Simple Chatbot with Streamlit")
    user_input = st.text_input("You: ", "")
    if user_input:
        response = simple_chatbot(user_input)
        if st.button("send"):
            st.text_area("Bot:", value=response, height=100)

if __name__== "__main__":
    main()
