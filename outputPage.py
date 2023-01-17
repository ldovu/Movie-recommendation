import streamlit as st
import backend as be
import inputPage 


#get query parameters
if st.experimental_get_query_params():
    value = st.experimental_get_query_params()["value"][0]
st.session_state.child = be.decode_string(value)


st.write("You are a" + st.sessione_state.child)