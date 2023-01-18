import streamlit as st
import backend as be
import pandas as pd

#get query parameters
values = st.experimental_get_query_params()["value"][0]

x =["child", "adult"]
for i in x:
    if i in values:
        st.write("user is " +i)

y= ["RIDERE","PIANGERE", "ADRENALINA", "AVVENTURA","AMORE", "PAURA", "FANTASTICARE", "SCIENCE FICTION", "CASUAL"]
for i in y:
    if i in values:
        st.write("mood is" + i)
    

           
    

           
res2 = values.split("fav=", 1)
#res3 = values.split("fav=", 1)
#res4 = values.split("time=", 1)
#for_child= be.decode_string(value)
#mood = be.decode_string(mood)
#film_target =be.decode_string(fav)
#Max = be.decode_string(time)

st.write( res2[1] )
