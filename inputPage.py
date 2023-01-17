import streamlit as st

st.title('Movie recommendation system')
st.header("AGE")
choiceAge =st.radio("Are you a child or an adult?", ["child","adult"], key="child",  index=0 )
       
def ifAdultShowMood(sessionAge):
    if sessionAge == "adult":
        st.header("MOOD")
        st.radio("Which emotion you would like to try?", ["RIDERE","PIANGERE", "ADRENALINA", "AVVENTURA","AMORE", "PAURA", "FANTASTICARE", "SCIENCE FICTION", "CASUAL"], key="visibility")
    
ifAdultShowMood(st.session_state.child)


st.header("SIMILARITY")
choicePreference = st.text_input('Which movie is similar to the one you want to watch?')

#if è per adulti allora no parte sotto
st.header("TIME")
choiceTime = st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
   
def selectTime(limitedTime):
    if limitedTime == 'limited':
        minute= st.slider('Select maximum minutes', 0, 360, 0)
        st.write("Yo have maximum:", minute, "minutes")
    
selectTime(st.session_state.minutes)