import streamlit as st
import backend as be
import pandas as pd

#get query parameters
values = st.experimental_get_query_params()["value"][0]



list1 = values.split('/?')

for_child = list1[0].replace("value=", "")
mood= list1[1].replace("mood=", "")
fav = list1[2].replace("fav=", "").replace("%20", " ")
time=list1[3].replace("time=", "")


st.write(for_child)
st.write(mood)
st.write(fav)
st.write(time)
#res3 = values.split("fav=", 1)
#res4 = values.split("time=", 1)
#for_child= be.decode_string(value)
#mood = be.decode_string(mood)
#film_target =be.decode_string(fav)
#Max = be.decode_string(time)
