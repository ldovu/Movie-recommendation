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
    

############################ MOVIE SELECTION ############################ 
st.header("SIMILARITY")

class MovieTarget:
    def __init__(self):
        st.text_input('Which movie is similar to the one you want to watch? (optional)', key="zxcvbn")

    def returnMovie(self):
        return st.session_state.zxcvbn

movie = MovieTarget()

############################ CHECK IF TITLE IS WRONG THEN RECOMMEND THE CORRECT ONE ############################
def checkInputUser(title):
    if di.checkTitolo(title) or title=="":
        st.write("You  would like to see a movie similar to ", title)
    else:
        
        mystring = ", ".join(di.forseCercavi(title))
          
        st.write("You might looked for: ", mystring)


checkInputUser(movie.returnMovie())

############################ CHECK IF TITLE IS WRONG THEN OUTPUT A BOOLEAN VALUE ############################
def checkInputUserBoolean(title):
    if di.checkTitolo(title) or title=="":
        return True
    else: 
        #st.error("Incorrect title movie")
        return False 

############################  TIME SELECTION  ############################ 
st.header("TIME")

class Time:
    def __init__(self):
        st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
        
    def returnTime(self):
        return st.session_state.minutes
       
time = Time()

class InputIn:
    def goToPage(self, movie, time):
        if time == "limited":
            st.slider('Select maximum minutes', 0, 360, 0, key="number")
                
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
                                              
                                        ''' % (True , movie, st.session_state.number), unsafe_allow_html=True)
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
                                              
                                        ''' % (True, movie, 600), unsafe_allow_html=True)
            if chat_botton :
                    nav_to("https://ldovu-movie-recommendation-outputpagechild-qi8pl4.streamlit.app/") 
    
                
inputs = InputIn()
inputs.goToPage(movie.returnMovie(), time.returnTime())


