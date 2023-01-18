import streamlit as st
import backend as be

#get query parameters
values = st.experimental_get_query_params()["value"][0]


res1 = values.split("value=", 1)
res2 = values.split("mood=", 1)
res3 = values.split("fav=", 1)
res4 = values.split("time=", 1)
#for_child= be.decode_string(value)
#mood = be.decode_string(mood)
#film_target =be.decode_string(fav)
#Max = be.decode_string(time)

st.write("for_child" + res1[1] + " \n mood" + res2[1] 
         + "\n sim to " + res3[1]+  "\n time"+res4[1]) 
