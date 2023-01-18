import streamlit as st
import backend as be
import pandas as pd

st.title('Movie recommendation system')

##############  AGE SELECTION  ##############
st.header("AGE")
choiceAge =st.radio("Are you a child or an adult?", ["child","adult"], key="child",  disabled=False )

encoded_age = be.encode_string(st.session_state.child)


if st.session_state.child=="adult":
    st.header("MOOD")
    df= pd.DataFrame(["RIDERE","PIANGERE", "ADRENALINA", 
                                      "AVVENTURA","AMORE", "PAURA",
                                        "FANTASTICARE", "SCIENCE FICTION", "CASUAL"])
    
    st.radio('Which emotion you would like to try?', df, key="banana")
    encoded_mood = be.encode_string(st.session_state.banana)
    
    ##############  MOOD SELECTION  ##############
    #if user is a child then do not show the option mood, otherwise yes
    st.header("SIMILARITY")
    choicePreference = st.text_input('Which movie is similar to the one you want to watch?', key="movieTarget")
    encoded_movieTarget = be.encode_string(st.session_state.movieTarget)

    ##############  TIME SELECTION  ############## 
    st.header("TIME")
    choiceTime = st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
       
    if st.session_state.minutes == 'limited':
            minute=st.slider('Select maximum minutes', 0, 360, 0)
            
            chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-outputpage-kldm4v.streamlit.app/?value=%s/?mood=%s/?fav=%s/?time=%s">
                                                 <button> Go to prediction movies </button>
                                             </a>
                                         </center>
                                     <div class="btn">
                                          
                                    ''' % (encoded_age,encoded_mood, encoded_movieTarget,minute), unsafe_allow_html=True)

    else:
            encoded_minute= be.encode_string(st.session_state.minutes)
            chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-outputpage-kldm4v.streamlit.app/?value=%s/?mood=%s/?fav=%s/?time=%s">
                                                 <button> Go to prediction movies </button>
                                             </a>
                                         </center>
                                     <div class="btn">
                                          
                                    ''' % (encoded_age, encoded_mood,encoded_movieTarget,encoded_minute), unsafe_allow_html=True)

else:
    ##############  MOVIE TARGET SELECTION  ##############
    st.header("SIMILARITY")
    choicePreference = st.text_input('Which movie is similar to the one you want to watch?', key="movieTarget")
    encoded_movieTarget = be.encode_string(st.session_state.movieTarget)

    ##############  TIME SELECTION  ##############
    
    st.header("TIME")
    choiceTime = st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
       
    if st.session_state.minutes == 'limited':
            minute=st.slider('Select maximum minutes', 0, 360, 0)
            
            chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-outputpage-kldm4v.streamlit.app/?value=%s/?fav=%s/?time=%s">
                                                 <button> Go to prediction movies </button>
                                             </a>
                                         </center>
                                     <div class="btn">
                                          
                                    ''' % (encoded_age, encoded_movieTarget,minute), unsafe_allow_html=True)

    else:
            encoded_minute= be.encode_string(st.session_state.minutes)
            chat_botton = st.write(f'''
                                     <div class="div">
                                         <center>
                                             <a href="https://ldovu-movie-recommendation-outputpage-kldm4v.streamlit.app/?value=%s/?fav=%s/?time=%s">
                                                 <button> Go to prediction movies </button>
                                             </a>
                                         </center>
                                     <div class="btn">
                                          
                                    ''' % (encoded_age,encoded_movieTarget,encoded_minute), unsafe_allow_html=True)



############################# REDIRECT TO PAGE 2 #####################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    
if chat_botton:
    nav_to("https://ldovu-movie-recommendation-outputpage-kldm4v.streamlit.app/")




