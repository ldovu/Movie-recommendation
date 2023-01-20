import streamlit as st
import backend as be
import pandas as pd
import numpy as np
import DatasetInspection as di

st.title('Movie recommendation system')


############################# REDIRECT TO PAGE 2 #####################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    

##############  MOVIE TARGET SELECTION  ##############
st.header("SIMILARITY")
choicePreference = st.text_input('Which movie is similar to the one you want to watch? (_optional_)', key="zxcvbn")

def timeSelection(timeOption, movie):
    if timeOption == 'limited':
            minute=st.slider('Select maximum minutes', 0, 360, 0)
            if checkInputUserBoolean(movie)==False :
                chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                                 <button  disabled="disabled"> Go to prediction movies </button>
                                         </center>
                                     <div class="btn">
                                          
                                    ''', unsafe_allow_html=True)
            else: 
                chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/?qwerty=%s/?zxcvbn=%s/?time=%s">
                                                 <button> Go to prediction movies </button>
                                             </a>
                                         </center>
                                     <div class="btn">
                                          
                                    ''' % (False , movie, minute), unsafe_allow_html=True)
            if chat_botton :
                nav_to("https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/")
           
    
    else:
        if checkInputUserBoolean(movie)==False :
                chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                                 <button  disabled="disabled"> Go to prediction movies </button>
                                         </center>
                                     <div class="btn">
                                          
                                    ''', unsafe_allow_html=True)
        else: 
            chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/?qwerty=%s/?zxcvbn=%s/?time=%s">
                                                 <button> Go to prediction movies </button>
                                             </a>
                                         </center>
                                     <div class="btn">
                                          
                                    ''' % (False, movie, 600), unsafe_allow_html=True)
            if chat_botton :
                nav_to("https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/") 
    
                

timeSelection(st.session_state.minutes, st.session_state.zxcvbn)

