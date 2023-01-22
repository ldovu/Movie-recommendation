import streamlit as st
import pandas as pd
import MovieRecommendationSystem as mrs
import numpy as np
import DatasetInspection as di

#get query parameters
values = st.experimental_get_query_params()["qwerty"][0]

list1 = values.split('/?')

child = list1[0].replace("qwerty=", "")
mood = ""
film_target = list1[1].replace("zxcvbn=", "").replace("%20", " ")
time =list1[2].replace("time=", "")


for_kids = True
Tmax = int(time)


m = mrs.MovieRecommendationSystem()
recommended = m.recommend(for_kids, mood,film_target, Tmax)

listRecom = recommended['title'].values

listOverview = []

st.header("Recommended movies:")


for i in range(len(listRecom)):
    value = di.trovaOverview(listRecom[i])
    listOverview.append(value)
    
   
        
col1, col2 = st.columns(2)

with col1:
    for i in range(0,10):
           st.write(f'''
                <div > <big><b>%d- %s </b></big>
                </div>
                ''' % (i+1, listRecom[i]), unsafe_allow_html=True)

    
with col2:
        
    option= st.selectbox("See the overview of", (listRecom[0],listRecom[1],listRecom[2],listRecom[3],listRecom[4],listRecom[5],listRecom[6],
                                                     listRecom[7],listRecom[8],listRecom[9]))
    st.write(di.trovaOverview(option))



