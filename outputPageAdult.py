import streamlit as st
import pandas as pd
import MovieRecommendationSystem as mrs


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
recommended = m.recommend(for_kids, mood, film_target, Tmax)
df = recommended.reset_index(drop=True)

st.write(df )

st.write(for_kids)
st.write(mood)
st.write(film_target)
st.write(time)

#prova link per i link delle trame dei film 
#url = "https://ldovu-movie-recommendation-page0-awd4vf.streamlit.app/"
#st.write("check out this [link](%s)" % url)


