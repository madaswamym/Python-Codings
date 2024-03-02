import pandas as pd
from sklearn.tree import DecisionTreeClassifier

movie_info = pd.read.csv("python_files/movieinterest.csv")
movie_info

input_dataset = movie_info.drop(coloums = ["interest"])
input_dataset


output_dataset = movie_info["interest"]
output_dataset


movie_model = DecisionTreeClassifier()
movie_model.fit(input_dataset,output_dataset)
movie_interest = movie_model.predict([9,1],[33,0])
movie_interest