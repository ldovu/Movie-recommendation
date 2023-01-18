import streamlit as st
from collections import defaultdict
#import backend as be

#get query parameters
values_dict = st.experimental_get_query_params()

for key, values in values_dict.iteritems():
    st.write("%s: %s", key, values)
