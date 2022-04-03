import streamlit as st
from utils.api import mypost
id_input = st.text_input('id', key='id')
mensaje_input = st.text_input('mensaje', key='mensaje')
if st.button('ok'):
    if (id_input and mensaje_input)!='':
        response = mypost(int(id_input),mensaje_input)
        st.write(response)

