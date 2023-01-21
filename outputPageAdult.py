import streamlit as st
import pandas as pd
import MovieRecommendationSystem as mrs
import numpy as np


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

listOverview = []

for i in range(recommended.shape[0]): #iterate over rows
    for j in range(recommended.shape[1]): #iterate over columns
        value = di.trovaOverview(recommended.at[i, j])
        listOverview.append(value)
        
st.write(recommended)

# Using 'Address' as the column name and equating it to the list
st.write(listOverview)




#df = recommended.reset_index(drop=True)






