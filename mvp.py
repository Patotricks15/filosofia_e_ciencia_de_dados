import streamlit as st
from main import citacoes

autor = st.text_input('Nome_Sobrenome: ')

if autor:
    st.pyplot(citacoes(autor, 2)[0])