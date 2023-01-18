import streamlit as st
import backend as be
import inputPage
import MovieRecommendationSystem as mrs 


#get query parameters
if st.experimental_get_query_params():
    value = st.experimental_get_query_params()["value"][0]
    mood =  st.experimental_get_query_params()["mood"][0]
    fav =  st.experimental_get_query_params()["fav"][0]
    time =   st.experimental_get_query_params()["time"][0]

for_child= be.decode_string(value)
mood = be.decode_string(mood)
film_target =be.decode_string(fav)
Max = be.decode_string(time)

st.write("You are a" + for_child + " mood of " +mood+ 
         " closest film " + film_target+ " max time" + Max )
