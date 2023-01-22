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
    
    
     
col1, col2, col3= st.columns(3)


with col1:
    st.write(f'''
         <div > <big><b> %s </b></big>
         </div>
         ''' % (listRecom[0]), unsafe_allow_html=True)
    expander = st.expander("See the overview", expanded=True)
    expander.write(listOverview[0] )
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[3]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[3] )
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[6]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[6] )
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[9]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[9] )
    
    
    
with col2:
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[1]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[1] )
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[4]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[4] )
    
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[7]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[7] )
    
    

with col3:
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[2]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[2] )
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[5]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[5] )
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write(f'''
        <div > <big><b> %s </b></big>
        </div>
        ''' % (listRecom[8]), unsafe_allow_html=True)
   
    expander = st.expander("See the overview")
    expander.write(listOverview[8] )
    
    
