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

for i in range(len(listRecom)):
    value = di.trovaOverview(listRecom[i])
    listOverview.append(value)
    
    
col1, col2, col3, col4, col5 = st.columns([3,3,3,3,3])


with col1:
    st.subheader(listRecom[0])
    expander = st.expander("See the overview")
    expander.write(listOverview[0] )
    
    st.write("")
    st.write("")
    
    st.subheader(listRecom[5])
    expander = st.expander("See the overview")
    expander.write(listOverview[5] )
    
    
with col2:
    st.subheader(listRecom[1])
    expander = st.expander("See the overview")
    expander.write(listOverview[1])
    
    st.write("")
    st.write("")
    
    st.subheader(listRecom[6])
    expander = st.expander("See the overview")
    expander.write(listOverview[6] )
    

with col3:
    st.subheader(listRecom[2])
    expander = st.expander("See the overview")
    expander.write(listOverview[2])
    
    st.write("")
    st.write("")
    
    st.subheader(listRecom[7])
    expander = st.expander("See the overview")
    expander.write(listOverview[7] )
    


with col4:
    st.subheader(listRecom[3])
    expander = st.expander("See the overview")
    expander.write(listOverview[3])
    
    st.write("")
    st.write("")
    
    st.subheader(listRecom[8])
    expander = st.expander("See the overview")
    expander.write(listOverview[8] )
    

with col5:
    st.subheader(listRecom[4])
    expander = st.expander("See the overview")
    expander.write(listOverview[4])
    
    st.write("")
    st.write("")
    
    st.subheader(listRecom[9])
    expander = st.expander("See the overview")
    expander.write(listOverview[9] )
    
    
    
