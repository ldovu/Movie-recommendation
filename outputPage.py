import streamlit as st
import backend as be
import pandas as pd

#get query parameters
values = st.experimental_get_query_params()["app"][0]

st.write(values.split('/?'))
