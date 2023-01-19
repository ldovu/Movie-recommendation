import streamlit as st
import backend as be
import pandas as pd
import numpy as np
import DatasetInspection as di

st.title('Movie recommendation system')

############################# REDIRECT TO PAGE  ############################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    

############################  MOOD SELECTION  ############################
st.header("MOOD")
df= pd.DataFrame(["laugh","cry", "adrenaline", "adventure","love", "fear", "fantasy", "science fiction", "casual"])

st.radio('Which emotion would you like to try?', df, key="asdfgh")


############################  MOVIE_TARGET SELECTION  ############################
st.header("SIMILARITY")
choicePreference = st.text_input('Which movie is similar to the one you want to watch? (_optional_)', key="zxcvbn")

   
if di.checkTitolo(st.session_state.zxcvbn) or st.session_state.zxcvbn=="":
        st.write("You  would like to see a movie similar to ", st.session_state.zxcvbn)
else:
    mystring = " "
    for x in di.forseCercavi(st.session_state.zxcvbn):
        mystring+= ' ' + x + ','
    st.write("You might looked for: ", mystring)

        
        
############################  TIME SELECTION  ############################ 
st.header("TIME")
choiceTime = st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
    


def timeSelection(timeOption, mood, movie):
    if timeOption == 'limited':
            minute=st.slider('Select maximum minutes', 0, 360, 0)
            #st.write("you have maximum: " + minute + " minutes")
            chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/?qwerty=%s/?asdfgh=%s/?zxcvbn=%s/?time=%s">
                                                 <button> Go to prediction movies </button>
                                             </a>
                                         </center>
                                     <div class="btn">
                                          
                                    ''' % (False,mood , movie, minute), unsafe_allow_html=True)
            if chat_botton :
                nav_to("https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/")
           
    
    else:
            #encoded_minute= be.encode_string(st.session_state.minutes)
            chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/?qwerty=%s/?asdfgh=%s/?zxcvbn=%s/?time=%s">
                                                 <button> Go to prediction movies </button>
                                             </a>
                                         </center>
                                     <div class="btn">
                                          
                                    ''' % (False, mood , movie, 600 ), unsafe_allow_html=True)
            if chat_botton:
                nav_to("https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/")


                                

timeSelection(st.session_state.minutes, st.session_state.asdfgh ,st.session_state.zxcvbn)
 
