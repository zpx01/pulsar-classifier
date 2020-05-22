import sklearn
from sklearn import neighbors,datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import seaborn as sns
from seaborn import palettes
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

# Converting data file to pandas DataFrame
data = pd.read_csv("HTRU_2.csv")

# Preprocessing the Data
pre = sklearn.preprocessing.LabelEncoder()
meanprof = pre.fit_transform(list(data["meanprof"]))
sd_prof = pre.fit_transform(list(data["sd-prof"]))
exk_prof = pre.fit_transform(list(data["exk-prof"]))
skewness_prof = pre.fit_transform(list(data["skewness-prof"]))
meandmsnr = pre.fit_transform(list(data["meandmsnr"]))
sd_dmsnr = pre.fit_transform(list(data["sd-dmsnr"]))
exk_dmsnr = pre.fit_transform(list(data["exk-dmsnr"]))
skewness_dmsnr = pre.fit_transform(list(data["skewness-dmsnr"]))
cls = pre.fit_transform(list(data["class"]))

# Pedicting class using KNN
predict = "class"

# Features
x = list(zip(meanprof, sd_prof, exk_prof, skewness_prof, meandmsnr, sd_dmsnr, exk_dmsnr, skewness_dmsnr))

# Predicting y-value
y = list(cls)


# Splitting data into Training/Testing datasets (test_size=z)
z = 0.2
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=z)

# KNN Model with n neighbors
n = 9 # Dynamically Change n (best accuracy at n=3, 6, 9)
model = KNeighborsClassifier(n_neighbors=n, weights='uniform', algorithm='ball_tree', p=1, n_jobs=-1)
model.fit(x_train, y_train)

# Accuracy
acc = model.score(x_test, y_test)
print(acc)

# Testing Model
predicted = model.predict(x_test)
names = ["pulsar", "non-pulsar"]

for x in range(len(x_test)): # Printing Predicted, Data, Actual, and n Values
    print("Predicted: ", names[predicted[x]], ", Data: ", x_test[x], ", Actual: ", names[y_test[x]], ", n: ", n)

