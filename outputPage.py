import streamlit as st
import backend as be
#get query parameters
values = st.experimental_get_query_params()["value"][0]

res = values.split("mood=", 1)


#for_child= be.decode_string(value)
#mood = be.decode_string(mood)
#film_target =be.decode_string(fav)
#Max = be.decode_string(time)

st.write(res[1])
