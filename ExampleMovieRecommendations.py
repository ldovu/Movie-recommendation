# in questo file se inserisci un film nella variabile film_preferito, ti restituisce 10 film 'simili'

import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from MovieRecommendation import Movie_Recommendation

dataset = pd.read_csv('movies_dataset.csv')
dataset = dataset.iloc[:,1:]

# inserire film
film_preferito = ''

# normalizzazione dei dati
d1 = dataset.iloc[:,1:]
sc = StandardScaler() 
sc.fit(d1) 
df_std = sc.transform(d1)

df = pd.DataFrame(df_std)
df.columns = d1.columns

titoli = pd.Series(dataset.iloc[:,0].values)
df["title"] = titoli

recommendations = Movie_Recommendation(df)

print("I 10 film raccomandati sono:")
print(recommendations.recommend(film_preferito, 10))
