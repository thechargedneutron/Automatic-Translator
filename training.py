import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, neighbors, svm
import pickle
import operator
import matplotlib.pyplot as plt
'''
Code to train the dataset. The same code was edited to train the English Alphabets.
'''
df = pd.read_csv('dataset.csv')
df = df.loc[(df['1023'] <= 256)]

df = df.sample(frac=0.2).reset_index(drop=True)

X = np.array(df.drop(['1024'],1))
y = np.array(df['1024'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size=0.2)

'''
Major training part. The dataset is trained and stored in a pickle file.
During the execution of application, the fitted estimator is fetched from the pickle file.
'''
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(2000, 1000),max_iter=500)
'''
The fit parameters can be changed to X, y while pickling at the end 
to increase the datasets (NOT during testing).
'''
mlp.fit(X_train,y_train)

with open('hindi.pickle','wb') as f:
	pickle.dump(mlp,f)

accuracy = mlp.score(X_test, y_test)
print("Done with an accuracy of {} percent".format(accuracy*100))
