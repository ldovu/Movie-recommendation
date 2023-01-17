import streamlit as st
import backend as be

st.title('Movie recommendation system')
st.header("AGE")
choiceAge =st.radio("Are you a child or an adult?", ["child","adult"], key="child",  index=0 )
       
def ifAdultShowMood(sessionAge):
    if sessionAge == "adult":
        st.header("MOOD")
        mood= st.radio("Which emotion you would like to try?", ["RIDERE","PIANGERE", "ADRENALINA", "AVVENTURA","AMORE", "PAURA", "FANTASTICARE", "SCIENCE FICTION", "CASUAL"], key="mood")
        st.write("you are in the " +mood+ " mood")

ifAdultShowMood(st.session_state.child)
clicked = st.button("You selected your age")
encoded_age = be.encode_string(st.session_state.child)

def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

if clicked:
    nav_to("https://ldovu-movie-recommendation-outputpage-kldm4v.streamlit.app/")

#if adult then show mood selection
def ifAdultShowMood(sessionAge):
    if sessionAge == "adult":
        st.header("MOOD")
        st.radio("Which emotion you would like to try?", ["RIDERE","PIANGERE", "ADRENALINA", "AVVENTURA","AMORE", "PAURA", "FANTASTICARE", "SCIENCE FICTION", "CASUAL"], key="visibility")
    
ifAdultShowMood(st.session_state.child)


st.header("SIMILARITY")
choicePreference = st.text_input('Which movie is similar to the one you want to watch?')

#if limited time then select time in the slider
st.header("TIME")
choiceTime = st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
   
def selectTime(limitedTime):
    if limitedTime == 'limited':
        minute= st.slider('Select maximum minutes', 0, 360, 0)
        st.write("Yo have maximum:", minute, "minutes")
    
selectTime(st.session_state.minutes)
