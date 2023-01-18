import streamlit as st
import backend as be

#get query parameters
if st.experimental_get_query_params():
    for_child = st.experimental_get_query_params()["value"][0]
    mood =  st.experimental_get_query_params()["mood"][0]
   # fav =  st.experimental_get_query_params()["fav"][0]
    #time =   st.experimental_get_query_params()["time"][0]


#mood = be.decode_string(mood)
#film_target =be.decode_string(fav)
#Max = be.decode_string(time)

st.write( for_child , mood)
