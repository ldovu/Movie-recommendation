#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:12:02 2023

@author: simonecossaro
"""

import unittest
import MovieRecommendationSystem3 as mr
import pandas as pd

dataset_movies = pd.read_csv('movies_dataset_overview.csv')
lista_titoli = dataset_movies['original_title']

################################################################################################

class Test_trovaOverview(unittest.TestCase):
    
    def test_overview(self):
        self.assertEqual(mr.trovaOverview('toy story'), 
                         "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
                         "Should be: Led by Woody, ...")
    def test_overview2(self):
        self.assertEqual(mr.trovaOverview('avatar'), 
                         "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.",
                         "Should be: In the 22nd century, ...")
        
################################################################################################

class Test_present(unittest.TestCase):
    
    def test_present(self):
        self.assertEqual(mr.ispresent(lista_titoli,'harry potter and the prisoner of azkaban'),
                        True, 'Should be True')
        
    def test_present2(self):
        self.assertEqual(mr.ispresent(lista_titoli,'big bang theory'), False, 'Should be False')

################################################################################################

class Test_checkTitolo(unittest.TestCase):
    
    def test_checktitolo(self):
        self.assertEqual(mr.checkTitolo('harry potter and the prisoner of azkaban'),
                        True, 'Should be True')
        
    def test_checktitolo2(self):
        self.assertEqual(mr.checkTitolo('big bang theory'), False, 'Should be False')

################################################################################################    

class Test_forseCercavi(unittest.TestCase):
    
    def test_forseCercavi(self):
        lista = mr.forseCercavi('avatr')
        presence = ('Avatar' in lista)
        self.assertEqual(presence,True,'Avatar should be present')
        
    def test_forseCercavi2(self):
        lista = mr.forseCercavi('harry potter')
        presence = ('Harry Potter and the Prisoner of Azkaban' in lista)
        self.assertEqual(presence,True,'HP3 should be present')
    
    def test_forseCercavi3(self):
        lista = mr.forseCercavi('meet the fockers')
        presence = ('Meet the Parents' in lista)
        self.assertEqual(presence,False,'Should not be present')

################################################################################################    

class Test_selectMovies(unittest.TestCase):
    
    def test_selectMovies(self):
        df = mr.selectMovies(dataset_movies,'RIDERE')
        pres = False
        for i in range(len(df.iloc[:,1])):
            if (df['Comedy'].iloc[i] == 0 or df['Drama'].iloc[i] == 1):
                pres = True
                break
        self.assertEqual(pres,False,'Should not be present drama films or not comedy films')
        
################################################################################################    

if __name__ == '__main__':
    unittest.main()
        

