import streamlit as st
import backend as be
import pandas as pd
import numpy as np

st.title('Movie recommendation system')

st.header("MOOD")
df= pd.DataFrame(["RIDERE","PIANGERE", "ADRENALINA", "AVVENTURA","AMORE", "PAURA", "FANTASTICARE", "SCIENCE FICTION", "CASUAL"])

st.radio('Which emotion you would like to try?', df, key="asdfgh")
#encoded_mood = be.encode_string(st.session_state.banana)

##############  MOOD SELECTION  ##############
#if user is a child then do not show the option mood, otherwise yes
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
                                         <a href="https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/?qwerty=adult/?asdfgh=%s/?zxcvbn=%s/?time=%s">
                                             <button> Go to prediction movies </button>
                                         </a>
                                     </center>
                                 <div class="btn">
                                      
                                ''' % ("adult",st.session_state.asdfgh ,st.session_state.zxcvbn, minute), unsafe_allow_html=True)

else:
        #encoded_minute= be.encode_string(st.session_state.minutes)
        chat_botton = st.write(f'''
                                 <div class="div">
                                     <center>
                                         <a href="https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/?qwerty=adult/?asdfgh=%s/?zxcvbn=%s/?time=%s">
                                             <button> Go to prediction movies </button>
                                         </a>
                                     </center>
                                 <div class="btn">
                                      
                                ''' % ("adult", st.session_state.asdfgh ,st.session_state.zxcvbn, np.Inf ), unsafe_allow_html=True)




############################# REDIRECT TO PAGE 2 #####################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    
if chat_botton:
    nav_to("https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/")

