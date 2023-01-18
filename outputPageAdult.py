import streamlit as st
import backend as be
import pandas as pd

#get query parameters
values = st.experimental_get_query_params()["qwerty"][0]

list1 = values.split('/?')

for_child = list1[0].replace("qwerty=", "")
mood= list1[1].replace("asdfgh=", "")
fav = list1[2].replace("zxcvbn=", "").replace("%20", " ")
time=list1[3].replace("time=", "")



st.write(for_child)
st.write(mood)
st.write(fav)
st.write(time)
