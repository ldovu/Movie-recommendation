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

recom = recommended['title'].values
#crea una colonna overview basata sulla colonna esistente di 
listOverview = []

for i in range(len(recom)): #iterate over rows 
    value= di.trovaOverview(recom[i])
    listOverview.append(value)
    
st.write(listOverview)


        
        
       
