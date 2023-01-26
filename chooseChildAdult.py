import streamlit as st
#styling
tabs_font_css = """
                <style> 
                    .btn{
                        border-radius: 5px;
                        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                      
                    }
                    h2 {
                      color: #0a0908;
                      }
                    
                    
                </style>
                """
st.write(tabs_font_css, unsafe_allow_html=True)

def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 6 ,1])
with col2:
    st.write(f'''
                             <h2> Let's start with your age </h2>
                                
                             
                            ''' , unsafe_allow_html=True)

    st.radio( "Are you an adult or a child?" , ["adult", "child"], key="qwerty")
    
    if st.session_state.qwerty == "adult":
        chat_botton1 = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-inputpageadult-n5m4a8.streamlit.app/?qwerty=%s">
                                                 <button> Move on </button>
                                             </a>
                                         </center>
                                     <div class="btn">

                                    ''' % (False), unsafe_allow_html=True)
        if chat_botton1 :
                nav_to("https://ldovu-movie-recommendation-inputpageadult-n5m4a8.streamlit.app/")
    elif st.session_state.qwerty == "child" :
        chat_botton2 = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-inputpagechild-wi5a4y.streamlit.app/?qwerty=%s">
                                                 <button> Move on </button>
                                             </a>
                                         </center>
                                     <div class="btn">

                                    ''' % (True), unsafe_allow_html=True)
        if chat_botton2 :
                nav_to("https://ldovu-movie-recommendation-inputpagechild-wi5a4y.streamlit.app/")
                
               


  


