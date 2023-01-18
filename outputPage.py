import streamlit as st
#import backend as be
from streamlit_javascript import st_javascript

#get query parameters


url = st_javascript("await fetch('').then(r => window.parent.location.href)")

st.write(url)


