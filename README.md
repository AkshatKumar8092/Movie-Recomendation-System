# Movie-Recomendation-System
with the help of machine learning i have made a ML model that will recommend us some similar moves based on or input





<----README.MD---->
to start the jupyter notebook *python -m notebook*
# <----libraries---->

import numpy as np
import pandas as pd
import ast
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle





What is recomendation system:

suppose we went to a shopping mall to pucrchase some cloths,
the shopkeeper will show us 10 different styles of cloths
in whoch we select some 1-2 cloths and ask them for something similar to that selected cloths


now what is ML in online recomendation system.
we browse for some movie in netflix or some other OTT platform now from that time onwards 
        then ML aslgorithm will only suggest me all the movies based on my browse selection

modern exampls of recomendation system are:
    spotify: it will only suggest the songs that are related to our likes
    amazon/flipkar: if i'm purchasing a mobile it will only recomend me to pucrchare the mobile cover and temperd glass togerther, 
            it should not suggest a toster to purchasing together with a mobile phone



basically it dosnt care about how to store,  it basically deals whith what to suggest and what all we should recomend to various user

Types of recomendation system:
    1. Content Based:
            as the name suggerst it will only recomend you on the base of Content
                example- if we are listning to some EDM songs it will only recoment the EDM song, Not some romantic song.
            recomend on the basis of similarities

    2. Collarabitive Filtiring Based:
            as per the user intreset it will recomend the next content

                A and B 2 users with similarity score is same assusme 9
                how to determine the similarites- both user watched some X webseries 'Money heist' once it complete they both give some similar rating then we can say that both person have some common intreset

                Now user A wathced some movie like avengers, now since both the user have given the same rating on money heist hence i will recomend avengers to user B as well
                
    3: Hybrid: 
            this is basically the combination og both content base recomend system and Collarabitive Filtiring based




in this project content based will be there



PROJECT FLOW:
    High level overview:

        DATA SET -> PRE-PROCESSING -> BUILDING A MODEIL (ml model) -> CONVERT IT TO WEBSITE -> DEPLOY THE WEBSITE

            DATA SET: we will find a data set that will be usefull for us
            PRE-PROCESSING: removing all the unwanted things from the data set
            MODEL BUILDING: bassically our ML Model that we will create.


            DATA SET: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

                

total movies 4860:  same as number of vectos.
for each vector we have to find the distance between the each vector

we won't use the ecudiliean distance formula insted we will find the angle between 2 vectors if both have less angle. hence we got our desired movie.


for this project its like 5000demension space

distacne is inversaly proportional to 1 by sine(thetha)


