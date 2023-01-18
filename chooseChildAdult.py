import streamlit as st

col1, col2, col3 = st.columns([1, 5,1])
with col2:
    with st.form:
        st.header("Let's start with your age")
        st.radio("Are you an adult o a child?", ["adult", "child"], key="qwerty")
        first = st.form_submit_button("Start")

def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

if first:
    if st.session_state.qwerty =="adult":
        nav_to("link to the page of the adult with mood")
    elif st.session_state.qwerty =="child":
        nav_to("link of the page of the child without mood")
