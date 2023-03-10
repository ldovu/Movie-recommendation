import streamlit as st

st.set_page_config(page_title="Movie recommendation")


############################################ REDIRECTION ############################################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

############################################ STYLING ############################################
tabs_font_css = """
                <style>
                [data-testid="stAppViewContainer"]{
                    background-color: #f1faee;
                    }
                    .btn{
                        border-radius: 5px;
                        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                      
                    }
                    .normal-text{
                        font-size: 20px;
                        color: #002642;
                        
                      }
                    
                    h1 {
                      color: #0a0908;
                      }
                    
                    p span {
                        display: block;
                    }
                    
                </style>
                """
st.write(tabs_font_css, unsafe_allow_html=True)

############################################ MAIN ############################################ 
col1, col2, col3 = st.columns([1, 15 ,1])
with col2:

    st.write(f'''
                                 <h1> Movie recommendation App </h1>
                                    <div class="normal-text">
                                        <p><span>Hi! </span> <span>This is a movie recommendation app. After answering a few questions, the system will suggest you 10 movies. </span><span>Take your time and enjoy:)</span>
                                        </p> 
                                    </div>




                                ''' , unsafe_allow_html=True)
    for i in range(1,3):
        st.write("") 

    chat_botton1 = st.write(f'''
                                  <div class="div">
                                      <center>
                                          <a href="https://ldovu-movie-recommendation-choosechildadult-abxz7g.streamlit.app/">
                                              <button> Start! </button>
                                          </a>
                                      </center>
                                  <div class="btn">

                                 ''', unsafe_allow_html=True)

    if chat_botton1 :
        nav_to("https://ldovu-movie-recommendation-choosechildadult-abxz7g.streamlit.app/")
