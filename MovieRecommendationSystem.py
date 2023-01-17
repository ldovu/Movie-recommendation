
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from tqdm import tqdm
import numpy as np

def recommendMovies(dataset, film_target, amount=1):
        distance = []
        # movie = i valori della riga del film
        movie = dataset[(dataset.title.str.lower() == film_target.lower())].head(1).values[0]
        # rec = il dataset a cui viene tolta la riga del film indicato
        rec = dataset[dataset.title.str.lower() != film_target.lower()]
        for film in tqdm(rec.values):
            d = 0
            for col in range(len(rec.columns)):
                if not col in [19]:
                    d = d + np.absolute(float(movie[col]) - float(film[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['title']
        return rec[columns][:amount]

# funzione che sceglie quali film tenere in base al mood    
def selectMovies(df, mood):
    if (mood == 'RIDERE'):
        return df[df.Comedy == 1]
    if (mood == 'PIANGERE'):
        return df[df.Drama == 1]
    if (mood == 'AMORE'):
        return df[df.Romance == 1]
    if (mood == 'ADRENALINA'):
        return df[df.Thriller == 1]
    if (mood == 'PAURA'):
        return df[df.Horror == 1]
    if (mood == 'FANTASTICARE'):
        return df[df.Fantasy == 1]
    if (mood == 'SCIENCE FICTION'):
        return df[df.ScienceFiction == 1]
    if (mood == 'AVVENTURA'):
        return df[df.Adventure == 1]
    if (mood == 'CASUAL'):
        return df
    return df

# funzione per vedere se il film è presente nel dataset anche dopo i tagli
def ispresent(lista, film):
    for x in lista:
        if (x.lower() == film.lower()):
            return True
    return False

class MovieRecommendationSystem():
    def __init__(self):
        self.dataset = pd.read_csv('movies_dataset.csv')
        self.dataset = self.dataset.iloc[:,1:]
    def recommend(self,for_kids,mood,film_target,Tmax ):
        if (not(film_target == None)):
            movie = pd.Series(self.dataset[(self.dataset.original_title.str.lower() == film_target.lower())].head(1).values[0], index = self.dataset.columns )  
        d1 = self.dataset.iloc[:,1:]
        # rimuovo film con durata maggiore di tmax
        d1 = d1[d1.runtime <= Tmax]
        self.dataset = self.dataset[self.dataset.runtime <= Tmax]
        # rimuovo film in base a for_kids
        if (for_kids):
            d1 = d1[d1.Animation == 1]
            self.dataset = self.dataset[self.dataset.Animation == 1]
        # rimuovo film in base a emotion
        if (not for_kids):
            d1 = selectMovies(d1,mood)
            self.dataset = selectMovies(self.dataset,mood)
        # se non è presente riaggiungo il film preferito
        if (not(film_target == None) and not ispresent(self.dataset.iloc[:,0],film_target)):
            d1.loc[len(d1)] = movie[1:19]
            self.dataset.loc[len(self.dataset)] = movie
        # normalizzazione dei dati
        sc = StandardScaler() 
        sc.fit(d1) 
        d1_std = sc.transform(d1)
        # riporto il dataset nel formato DataFrame
        d2 = pd.DataFrame(d1_std)
        d2.columns = d1.columns
        # aggiungo i titoli dei film
        titoli = self.dataset.iloc[:,0].values
        d2["title"] = titoli
        
        recommendations = recommendMovies(d2,film_target,10)
   
        return recommendations
