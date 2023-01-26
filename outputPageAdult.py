import streamlit as st
import pandas as pd
import MovieRecommendationSystem as mrs
import numpy as np
import DatasetInspection as di
import backend

st.set_page_config(page_title="Movie recommendation")

############################# STYLING #############################
tabs_font_css = """
                <style>
                    .btn{
                        border-radius: 5px;
                        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                      
                    }
                    
                    h2 {
                      color: #002642;
                    }
                    h1 {
                      color: #0a0908;
                      }
                    
                    
                </style>
                """
st.write(tabs_font_css, unsafe_allow_html=True)

#get query parameters
values = st.experimental_get_query_params()["qwerty"][0]


list1 = values.split('/?')

child = list1[0].replace("qwerty=", "")
mood = list1[1].replace("asdfgh=", "")
film_target = list1[2].replace("zxcvbn=", "").replace("%20", " ")
time = list1[3].replace("time=", "")

for_kids = False
Tmax = int(time)
  

m = mrs.MovieRecommendationSystem()
recommended = m.recommend(for_kids, mood, film_target , Tmax )

listRecom = recommended['title'].values


listOverview = []

st.write(f'''
                 <h1> Movie recommendation App </h1><h2> Recommended movies: </h2>
             ''' , unsafe_allow_html=True)


for i in range(len(listRecom)):
    value = di.trovaOverview(listRecom[i])
    listOverview.append(value)
    
        
col1, col2 = st.columns(2)

with col1:
    for i in range(0,10):
           st.write(f'''
                <div > <big><b>%d -</b>  %s </big>
                </div>
                ''' % (i+1, listRecom[i]), unsafe_allow_html=True)

    
with col2:
        
    option= st.selectbox("Read the overview of", (listRecom[0],listRecom[1],listRecom[2],listRecom[3],listRecom[4],listRecom[5],listRecom[6],
                                                     listRecom[7],listRecom[8],listRecom[9]))
    st.write(di.trovaOverview(option))

        
       
