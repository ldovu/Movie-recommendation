import streamlit as st
import pandas as pd
import MovieRecommendationSystem as mrs
import numpy as np
import DatasetInspection as di


#get query parameters
values = st.experimental_get_query_params()["qwerty"][0]

list1 = values.split('/?')

child = list1[0].replace("qwerty=", "")
mood = list1[1].replace("asdfgh=", "")
film_target = list1[2].replace("zxcvbn=", "").replace("%20", " ")
time =list1[3].replace("time=", "")

for_kids = False
Tmax = int(time)
  

m = mrs.MovieRecommendationSystem()
recommended = m.recommend(for_kids, mood, film_target , Tmax )

listRecom = recommended['title'].values


listOverview = []

for i in range(len(listRecom)): #iterate over rows 
    value= di.trovaOverview(listRecom[i])
    listOverview.append(value)

for j in range(len(listOverview)):
    expander = st.expander("See the overview")
    expander.write(j)

        
        
       
