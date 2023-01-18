import streamlit as st
import backend as be
import pandas as pd
import numpy as np

st.title('Movie recommendation system')



##############  MOVIE TARGET SELECTION  ##############
st.header("SIMILARITY")
choicePreference = st.text_input('Which movie is similar to the one you want to watch?', key="zxcvbn")
#encoded_movieTarget = be.encode_string(st.session_state.movieTarget)

##############  TIME SELECTION  ##############

st.header("TIME")
choiceTime = st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
   
if st.session_state.minutes == 'limited':
        minute=st.slider('Select maximum minutes', 0, 360, 0)
        #st.write("you have maximum: " + minute + " minutes")
        chat_botton = st.write(f'''
                                 <div class="div">
                                     <center>
                                         <a href="https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/?qwerty=%s/?zxcvbn=%s/?time=%s">
                                             <button> Go to prediction movies </button>
                                         </a>
                                     </center>
                                 <div class="btn">
                                      
                                ''' % ("child",st.session_state.zxcvbn, minute), unsafe_allow_html=True)

else:
        #encoded_minute= be.encode_string(st.session_state.minutes)
        chat_botton = st.write(f'''
                                 <div class="div">
                                     <center>
                                         <a href="https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/?qwerty=%s/?zxcvbn=%s/?time=%s">
                                             <button> Go to prediction movies </button>
                                         </a>
                                     </center>
                                 <div class="btn">
                                      
                                ''' % ("child",st.session_state.zxcvbn, np.Inf ), unsafe_allow_html=True)




############################# REDIRECT TO PAGE 2 #####################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    
if chat_botton:
    nav_to("https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/")
