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



set_background('sfondo.png')

#styling
tabs_font_css = """
                <style>
                    div[class*="sttitle"] label {
                      font-size: 20px;
                      font-family: "Georgia, serif", monospace;
                      text-align: Center;
                      color: Red;
                    }
                    div[class*="stwrite"] label {
                      font-size: 20px;
                      font-family:  "Georgia, serif", monospace;
                      text-align: Center;
                      color: Orange;
                    }
                </style>
                """
st.write(tabs_font_css, unsafe_allow_html=True)


st.write(f'''
             <b style="font-family:Georgia,serif; color:Red; font-size: 20px;"> Movie recommendation system</b>
          ''', unsafe_allow_html=True)

def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)


with st.form("Welcome box"):
        st.write("Hi!  \n  This is a movie recommendation system and it will take a few time to answer this questions  \n\n take your time and enjoy:)")
        first = st.form_submit_button("Start")

if first:
    nav_to("https://ldovu-movie-recommendation-choosechildadult-abxz7g.streamlit.app/")


