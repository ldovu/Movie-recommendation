import streamlit as st


st.title("Movie recommendation system")

with st.form("Welcome box"):
        st.write("Hi!  \n  This is a movie recommendation system and it will take a few time to answer this questions  \n\n take your time and enjoy:)")
        first = st.form_submit_button("Start")
    
