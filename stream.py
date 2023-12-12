import streamlit as st

def simple_chatbot(user_input):
    user_input = user_input.lower()
    if 'my name' in user_input:
        return 'your name is VARUNA'
    elif 'my mother' in user_input:
        return 'your mother name is KAMACHI.\n I know she is very HARD WORKING women.\n She look very BEAUTIFUL'
    elif 'father' in user_input:
        return 'your father name is SUGUMAR\n He is a ORDINARY PERSON.'
    elif 'brother' in user_input:
        return ('your brother name is DIVID ...\n its amazing it is a palindrom letter right...')
    elif 'divid' in user_input:
        return ('Divid best friend is ISHWARYA..\n she is also cute , But not like DIVID.because divid is a handsome guy')
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
