import streamlit as st


st.title("Movie recommendation system")

def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)


with st.form("Welcome box"):
        st.write("Hi!  \n  This is a movie recommendation system and it will take a few time to answer this questions  \n\n take your time and enjoy:)")
        first = st.form_submit_button("Start")
    
if first:
    nav_to("https://ldovu-movie-recommendation-inputpage-1y1p3j.streamlit.app/")
