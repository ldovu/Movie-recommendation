import streamlit as st
import backend as be

values =[] 
query = ["value","mood", "fav", "time"]
for i in query:
    values = st.experimental_get_query_params()[i][0]
    

#for_child= be.decode_string(value)
#mood = be.decode_string(mood)
#film_target =be.decode_string(fav)
#Max = be.decode_string(time)

st.write(values)
