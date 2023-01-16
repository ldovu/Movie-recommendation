from MovieRecommendation import Movie_Recommendation
from MovieRecommendation import Movie_Recommendation_SameCluster
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

#   INPUT UTENTE:

#   1) PER BAMBINO?
#       - SI ------> solo animation
#       - NO ------> tutto

#   2) FILM PREFERITO  ------- OK

#   3) COSA VUOI DAL FILM?
#       - RIDERE    ------> comedy
#       - PIANGERE  ------> drama
#       - ADRENALINA -----> thriller
#       - AVVENTURA  -----> adventure
#       - AMORE     ------> romance
#       - PAURA     ------> horror
#       - FANTASTICARE ---> fantasy
#       - SCIENCE FICTION -> science fiction
#       - VA BENE TUTTO

#   4) QUANTO TEMPO HAI A DISPOSIZIONE?
#       - NO LIMITI 
#       - IMPONGO UN LIMITE Tmax


for_kids = False
film_preferito = ''
i_want = 'va bene tutto'
Tmax = np.Inf

def onlyGenresMovies(df, i_want):
    if (i_want == 'ridere'):
        return df[df.Comedy == 1]
    if (i_want == 'piangere'):
        return df[df.Drama == 1]
    if (i_want == 'amore'):
        return df[df.Romance == 1]
    if (i_want == 'adrenalina'):
        return df[df.Thriller == 1]
    if (i_want == 'paura'):
        return df[df.Horror == 1]
    if (i_want == 'fantasticare'):
        return df[df.Fantasy == 1]
    if (i_want == 'science fiction'):
        return df[df.ScienceFiction == 1]
    if (i_want == 'avventura'):
        return df[df.Adventure == 1]
    if (i_want == 'va bene tutto'):
        return df
    return df

def ispresent(lista, film):
    for x in lista:
        if (x.lower() == film.lower()):
            return True
    return False
  
dataset = pd.read_csv('movies_dataset.csv')
dataset = dataset.iloc[:,1:]

movie = pd.Series(df_titolo[(df_titolo.original_title.str.lower() == film_preferito.lower())].head(1).values[0], index = df_titolo.columns )

d1 = d1.iloc[:,1:]

# rimuovo film con durata maggiore
d2 = d2[d2.runtime <= Tmax]

dataset = dataset[dataset.runtime <= Tmax]

# rimuovo film in base a for_kids
if (for_kids):
    d2 = d2[d2.Animation == 1]
    dataset = dataset[dataset.Animation == 1]
    
# rimuovo film in base a i_want
if (not for_kids):
    d2 = onlyGenresMovies(d2,i_want)
    dataset = onlyGenresMovies(dataset,i_want)
    
if (not ispresent(dataset.iloc[:,0],film_preferito)):
    d2.loc[len(d2)] = movie[1:20]
    dataset.loc[len(dataset)] = movie
    
# normalizzazione dei dati
sc = StandardScaler() 
sc.fit(d2) 
d2_std = sc.transform(d2)

d3 = pd.DataFrame(d2_std)
d3.columns = d2.columns

# aggiungo i titoli dei film
titoli = dataset.iloc[:,0].values
d3["title"] = titoli

recommendations = Movie_Recommendation(d3)

print("I 10 film raccomandati sono:")
print(recommendations.recommend(film_preferito, 10))
