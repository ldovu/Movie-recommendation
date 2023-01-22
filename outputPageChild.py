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

for i in range(len(listRecom)): #iterate over rows 
    value = di.trovaOverview(listRecom[i])
    listOverview.append(value)
    st.write(listRecom[i])
    
    expander = st.expander("See the overview")
    expander.write(listOverview[i] )
    
