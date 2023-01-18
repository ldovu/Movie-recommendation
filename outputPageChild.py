import streamlit as st
import pandas as pd
import MovieRecommendationSystem as mrs

#get query parameters
values = st.experimental_get_query_params()["qwerty"][0]

list1 = values.split('/?')

child = list1[0].replace("qwerty=", "")
fav = list1[1].replace("zxcvbn=", "").replace("%20", " ")
time =list1[2].replace("time=", "")

for_kids = False
Tmax= int(time)


m = mrs.MovieRecommendationSystem()
recommended = m.recommend(for_kids, film_target, Tmax)
st.write(recommended )
