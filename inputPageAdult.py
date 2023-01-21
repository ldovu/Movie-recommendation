import streamlit as st
import pandas as pd
import DatasetInspection as di


st.title('Movie recommendation system')

############################# REDIRECT TO PAGE  ############################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    

############################  MOOD SELECTION  ############################
#st.header("MOOD")
df= pd.DataFrame(["laugh","cry", "adrenaline", "adventure","love", "fear", "fantasy", "science fiction", "casual"])

class Mood:
    st.header("MOOD")
    def __init__(self):
        st.radio('Which emotion would you like to try?', df, key="asdfgh")

    def returnMood(self):
        return st.session_state.asdfgh
        
mood = Mood() #create an object mood

############################ MOVIE SELECTION ############################ 
class MovieTarget:
    def __init__(self):
        st.header("SIMILARITY")
        st.text_input('Which movie is similar to the one you want to watch? (optional)', key="zxcvbn")

    def returnMovie(self):
        return st.session_state.zxcvbn

movie = MovieTarget()


############################ CHECK USER INPUT ############################
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


class Time:
    def __init__(self):
        st.header("TIME")
        st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
        
    def returnTime(self):
        return st.session_state.minutes
       
time = Time()

class InputIn:  
    def goToPage(self, mood, movie, time):
        if time =="limited":
            st.slider('Select maximum minutes', 0, 360, 0, key="number" )
            
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
                                                 <a href="https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/?qwerty=%s/?asdfgh=%s/?zxcvbn=%s/?time=%s">
                                                     <button> Go to prediction movies </button>
                                                 </a>
                                             </center>
                                         <div class="btn">
                                              
                                        ''' % (False, mood, movie, st.session_state.number), unsafe_allow_html=True)
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
                                                 <a href="https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/?qwerty=%s/?asdfgh=%s/?zxcvbn=%s/?time=%s">
                                                     <button> Go to prediction movies </button>
                                                 </a>
                                             </center>
                                         <div class="btn">
                                              
                                        ''' % (False, mood, movie, 600), unsafe_allow_html=True)
        
        if chat_botton :
                    nav_to("https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/")
               
  
inputs = InputIn()
inputs.goToPage(mood.returnMood(), movie.returnMovie(), time.returnTime())























