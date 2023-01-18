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
    
    if st.session_state.qwerty =="adult":
        chat_botton1 = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-inputpageadult-45z3ld.streamlit.app/?qwerty=%s">
                                                 <button> Move to the next question </button>
                                             </a>
                                         </center>
                                     <div class="btn">

                                    ''' % (st.session_state.qwerty), unsafe_allow_html=True)
        if chat_botton1 :
                nav_to("https://ldovu-movie-recommendation-inputpageadult-45z3ld.streamlit.app/")
    elif st.session_state.qwerty =="child":
        chat_botton2 = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-inputpagechild-2jx062.streamlit.app/?qwerty=%s">
                                                 <button> Move to the next question </button>
                                             </a>
                                         </center>
                                     <div class="btn">

                                    ''' % (st.session_state.qwerty), unsafe_allow_html=True)
        if chat_botton2 :
                nav_to("https://ldovu-movie-recommendation-inputpagechild-2jx062.streamlit.app/")
                
               


