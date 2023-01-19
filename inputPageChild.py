import streamlit as st
import backend as be
import pandas as pd
import numpy as np
import DatasetInspection as di

st.title('Movie recommendation system')



##############  MOVIE TARGET SELECTION  ##############
st.header("SIMILARITY")
choicePreference = st.text_input('Which movie is similar to the one you want to watch? (_optional_)', key="zxcvbn")

def checkUserInput(title):
    if di.checkTitolo(title) or title=="":
        st.write("You  would like to see a movie similar to ", title)
    else:
        mystring = ", ".join(di.forseCercavi(title))
        st.write("You might looked for: ", mystring)

checkUserInput(st.session_state.zxcvbn)


##############  TIME SELECTION  ##############

st.header("TIME")
choiceTime = st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
   
def timeSelection(timeOption, movie):
    if timeOption == 'limited':
        minute=st.slider('Select maximum minutes', 0, 360, 0)
        
        chat_botton = st.write(f'''
                                 <div class="div">
                                     <center>
                                         <a href="https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/?qwerty=%s/?zxcvbn=%s/?time=%s">
                                             <button> Go to prediction movies </button>
                                         </a>
                                     </center>
                                 <div class="btn">
                                      
                                ''' % (True ,movie , minute), unsafe_allow_html=True)
    else:
        
        chat_botton = st.write(f'''
                                 <div class="div">
                                     <center>
                                         <a href="https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/?qwerty=%s/?zxcvbn=%s/?time=%s">
                                             <button> Go to prediction movies </button>
                                         </a>
                                     </center>
                                 <div class="btn">
                                      
                                ''' % (True,movie , 600 ), unsafe_allow_html=True)

timeSelection(st.session_state.minutes, st.session_state.zxcvbn)



############################# REDIRECT TO PAGE 2 #####################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    
if chat_botton:
    nav_to("https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/")

