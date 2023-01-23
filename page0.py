import streamlit as st
import base64

st.set_page_config(page_title="Movie recommendation", page_icon="💯")


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#function to set the background
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
                    <style>
                        .stApp {
                            background-image: url("data:image/png;base64,%s");
                            background-size: cover;
                        }
                    </style>
                  ''' % (bin_str)
    st.markdown(page_bg_img, unsafe_allow_html=True)


#redirection to
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

#set_background('sfondo.png')

#styling
tabs_font_css = """
                <style>
                    .btn{
                        border-radius: 5px;
                        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                      
                    }
                    .header{
                        border: 1px ;
                        position: fixed;
                        color: red;
                        font-family: Segoe UI;
                        
                    }
                    .normal-text{
                        font-size: 20px;
                        color: black;
                        font-family: Segoe UI;
                    }
                    p span {
                        display: block;
                    }
                    
                </style>
                """
st.write(tabs_font_css, unsafe_allow_html=True)


st.write(f'''
                             <div class="header" > 
                                 <h1> Movie recommendation system </h1>
                                    <div class="normal-text"> 
                                        <p><span>Hi! This is a movie recommandation system. It will take a few time to answer this questions</span><span>Take your time and enjoy:)</span>
                                        </p> 
                                    </div>
                             </div>
                             
                             

                            ''' , unsafe_allow_html=True)
for i in range(1,10):
    st.write("") 

chat_botton1 = st.write(f'''
                              <div class="div">
                                  <center>
                                      <a href="https://ldovu-movie-recommendation-choosechildadult-abxz7g.streamlit.app/">
                                          <button> Move to the next question </button>
                                      </a>
                                  </center>
                              <div class="btn">

                             ''', unsafe_allow_html=True)

if chat_botton1 :
    nav_to("https://ldovu-movie-recommendation-choosechildadult-abxz7g.streamlit.app/")


