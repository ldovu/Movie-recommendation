import streamlit as st
import pandas as pd
import MovieRecommendationSystem as mrs


#get query parameters
values = st.experimental_get_query_params()["qwerty"][0]

list1 = values.split('/?')

for_kids = list1[0].replace("qwerty=", "")
mood= list1[1].replace("asdfgh=", "")
film_target = list1[2].replace("zxcvbn=", "").replace("%20", " ")
Tmax=list1[3].replace("time=", "")

m = mrs.MovieRecommendationSystem()
recommended = m.recommend(for_kids, mood, film_target, Tmax)
