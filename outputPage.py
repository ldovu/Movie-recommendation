import streamlit as st
from collections import defaultdict
#import backend as be

#get query parameters

for key, values in st.experimental_get_query_params():
    st.write("%s: %s", key, values)

