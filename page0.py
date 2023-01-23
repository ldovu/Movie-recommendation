import streamlit as st
import base64

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

set_background('sfondo.png')

#styling
tabs_font_css = """
                <style>
                    .btn{
                        padding: 8px 28px;
                        background: white;
                        display:inline-block;
                        color: white;
                        border-radius: 5px;
                      
                    }
                    .header{
                        border: 1px ;
                        position: fixed;
                        color:red;
                        font-family:Segoe UI;
                        
                    }
                </style>
                """
st.write(tabs_font_css, unsafe_allow_html=True)

st.write(f'''
            <div class="header"> <h1> Movie recommandation system </h1><div>
         ''', unsafe_allow_html=True)



st.write("Hi!  \n  This is a movie recommendation system and it will take a few time to answer this questions  \n\n take your time and enjoy:)")
first = st.write(f'''
                             <div class="btn">
                                 <center>
                                        <button> Start </button>
                                     </a>
                                 </center>
                             <div>

                            ''' , unsafe_allow_html=True)

if first:
    nav_to("https://ldovu-movie-recommendation-choosechildadult-abxz7g.streamlit.app/")



