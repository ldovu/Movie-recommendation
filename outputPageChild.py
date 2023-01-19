import streamlit as st
import pandas as pd
import MovieRecommendationSystem as mrs

#get query parameters
values = st.experimental_get_query_params()["qwerty"][0]

list1 = values.split('/?')

child = list1[0].replace("qwerty=", "")
film_target = list1[1].replace("zxcvbn=", "").replace("%20", " ")
time =list1[2].replace("time=", "")
mood = ""

for_kids = True
Tmax = int(time)


m = mrs.MovieRecommendationSystem()
recommended = m.recommend(for_kids, mood,film_target, Tmax)
st.write(recommended )
