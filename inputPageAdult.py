import streamlit as st
import pandas as pd
import DatasetInspection as di


############################# REDIRECT TO PAGE  ############################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    

############################# STYLING #############################
tabs_font_css = """
                <style>
                    .btn{
                        border-radius: 5px;
                        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                      
                    }
                    
                    h2 {
                      color: #002642;
                    }
                    h1 {
                      color: #0a0908;
                      }
                    
                    
                </style>
                """
st.write(tabs_font_css, unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 15 ,1])
with col2:
    ############################  MOOD SELECTION  ############################
    st.write(f'''
                     <h1> Movie recommendation App </h1><h2> MOOD </h2>
                 ''' , unsafe_allow_html=True)
    df= pd.DataFrame(["laugh","cry", "adrenaline", "adventure","love", "fear", "fantasy", "science fiction", "casual"])
    st.radio('Which emotion would you like to try?', df, key="asdfgh")


    ############################ MOVIE SELECTION ############################ 
    st.write(f'''
                     <h2> SIMILARITY </h2>
                 ''' , unsafe_allow_html=True)
    st.text_input('Which movie is similar to the one you want to watch? (*optional*)', key="zxcvbn")


    ############################ CHECK USER INPUT ############################
    def checkInputUser(title):
        if di.checkTitolo(title) or title=="":
            st.write("You  would like to see a movie similar to: ", title)
        else:

            mystring = ", ".join(di.forseCercavi(title))

            st.write(":warning: Incorrect title! You might looked for: ", mystring)


    checkInputUser(st.session_state.zxcvbn)

    ############################ CHECK IF TITLE IS WRONG THEN OUTPUT A BOOLEAN VALUE ############################
    def checkInputUserBoolean(title):
        if di.checkTitolo(title) or title=="":
            return True
        else: 
            return False 



    ############################  TIME SELECTION  ############################
    st.write(f'''
                     <h2> TIME </h2>
                 ''' , unsafe_allow_html=True)
    st.radio("How much time do you have?", ["infinite","limited"], key="minutes")

    ############################ MAIN FUNCTION ############################
    def goToPage(mood, movie, time):
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

                                            ''' % (False,mood, movie , 600), unsafe_allow_html=True)

            if chat_botton :
                        nav_to("https://ldovu-movie-recommendation-outputpageadult-45fjq9.streamlit.app/")



    goToPage(st.session_state.asdfgh, st.session_state.zxcvbn , st.session_state.minutes )


