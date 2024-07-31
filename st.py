import streamlit as st

st.title('Hiii')

# Text input
user_input = st.text_input('Enter some text:')

# Display the user input
st.write('You entered:', user_input)

