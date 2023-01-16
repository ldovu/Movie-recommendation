from tqdm import tqdm
import numpy as np

class Movie_Recommendation():
    def __init__(self, dataset):
        self.dataset = dataset
    def recommend(self, movies, amount=1):
        distance = []
        # movie = i valori della riga del primo film che trova nel dataset con quel titolo
        movie = self.dataset[(self.dataset.title.str.lower() == movies.lower())].head(1).values[0]
        # rec = il dataset a cui viene tolta la riga del film indicato
        rec = self.dataset[self.dataset.title.str.lower() != movies.lower()]
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
