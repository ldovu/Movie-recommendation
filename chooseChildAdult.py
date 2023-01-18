import streamlit as st

def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 6 ,1])
with col2:
    st.header("Let's start with your age")
    st.radio("Are you an adult o a child?", ["adult", "child"], key="qwerty")
    
    chat_botton = st.write(f'''
                                 <div class="div">
                                     <center>
                                         <a href="/?qwerty=%s">
                                             <button> Move to the next question </button>
                                         </a>
                                     </center>
                                 <div class="btn">
                                      
                                ''' % (st.session_state.qwerty), unsafe_allow_html=True)

    if chat_botton() :
            if st.session_state.qwerty =="adult":
                nav_to("link to the page of the adult with mood")
            elif st.session_state.qwerty =="child":
                nav_to("link of the page of the child without mood")


