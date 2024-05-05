# -*- coding: utf-8 -*-
"""mL with python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DQXezb8na20gHMfL6B6GQiZ4AoWcpMP9
"""

from google.colab import files
uploaded=files.upload()

import pandas as pd
import io

df = pd.read_csv(io.BytesIO(uploaded['vgsales (1).csv']))

df.shape

df.describe()

df.values

from google.colab import files
uploaded=files.upload()

import pandas as pd
import io
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
music_data= pd.read_csv(io.BytesIO(uploaded['music.csv']))
X= music_data.drop(columns=['genre'])
y=music_data['genre']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
model =DecisionTreeClassifier()
model.fit(X_train,y_train)
predictions=model.predict(X_test)
score=accuracy_score(y_test,predictions)
score

import pandas as pd
import io
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
music_data= pd.read_csv(io.BytesIO(uploaded['music.csv']))
X= music_data.drop(columns=['genre'])
y=music_data['genre']
model =DecisionTreeClassifier()
model.fit(X,y)
tree.export_graphviz(model,out_file='music-recommender.dot',
                     feature_names=['age','gender'],
                     class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True
                     )