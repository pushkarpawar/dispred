import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("new_training_data.csv")


features = data.iloc[:,:-1]
target = data['prognosis']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.25, random_state = 1)


from sklearn.metrics import accuracy_score


#KNN
from sklearn.neighbors import KNeighborsClassifier

KN = KNeighborsClassifier(n_neighbors =4)
modelKN = KN.fit(X_train,y_train)


import pickle
with open('ml_algo_pred.pkl', 'wb') as file:
    pickle.dump(modelKN, file)