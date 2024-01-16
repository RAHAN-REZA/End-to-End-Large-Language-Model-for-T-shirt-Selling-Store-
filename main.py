from langchain_helper import get_few_shot_db_chain

import streamlit as st

st.title("RZYN 👕 : Database Q&A ")

question = st.text_input("HOW MAY I HELP YOU 😇 :")
if question:
    chain = get_few_shot_db_chain()
    answer = chain.run(question)
    st.header("Answer:")
    st.write(answer)