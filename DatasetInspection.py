import pandas as pd
from Levenshtein import distance

###########################################################

dataset_movies = pd.read_csv('movies_dataset_overview.csv')

###########################################################

def checkTitolo(titolo):
        for i in range(len(dataset_movies['original_title'])):
                if (titolo.lower() == dataset_movies['original_title'][i].lower()):
                        return True
        return False

###########################################################

def forseCercavi(film):
        lista = []
        for i in range(len(dataset_movies['original_title'])):
                if (film.lower() in str(dataset_movies['original_title'][i].lower())):
                        lista.append(dataset_movies['original_title'][i])
                elif (distance(film.lower(),dataset_movies['original_title'][i].lower()) <= 2):
                        lista.append(dataset_movies['original_title'][i])
        return lista
    
###########################################################

def trovaOverview(film):
    for i in range(len(dataset_movies['original_title'])):
        if (dataset_movies['original_title'][i].lower() == film.lower()):
            return dataset_movies['overview'][i]
    return None
    
###########################################################
