#!/usr/bin/python

import matplotlib.pyplot as plt
from time import time
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################
def acc_score(x,y):
    acc = accuracy_score(x,y)
    return "Accuracy score is {}".format(round(acc, 3))

#KNeighborsClassifier

print ('KNeighborsClassifier')
t0 = time()
clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(features_train, labels_train)
print ("training time on fitting:", round(time()-t0, 3), "s")
t0 = time()
pred = clf.predict(features_test)
print ("training time on prediction:", round(time()-t0, 3), "s")
print (acc_score(labels_test, pred), '\n')

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

#RandomForestClassifier - begging algorithm
print ('RandomForestClassifier')
t0 = time()
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(features_train, labels_train)
print ("training time on fitting:", round(time()-t0, 3), "s")
t0 = time()
pred = clf.predict(features_test)
print ("training time on prediction:", round(time()-t0, 3), "s")
print (acc_score(labels_test, pred), '\n')


# AdaBoostClassifier - boosting algorithm
print ('AdaBoostClassifier')
t0 = time()
clf = AdaBoostClassifier(base_estimator=None, n_estimators=10, learning_rate=1.0, algorithm='SAMME.R', random_state=None)
clf.fit(features_train, labels_train)
print ("training time on fitting:", round(time()-t0, 3), "s")
t0 = time()
pred = clf.predict(features_test)
print ("training time on prediction:", round(time()-t0, 3), "s")
print (acc_score(labels_test, pred), '\n')


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary









