#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")
from tools.email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# optimal param for rbf-kernel is C = 10000
clf = SVC(kernel="rbf", C=10000)
t0 = time()
# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]
clf.fit(features_train,labels_train)
print ("training time on fitting:", round(time()-t0, 3), "s")
t0 = time()
pred = clf.predict(features_test)
print ("training time on prediction:", round(time()-t0, 3), "s")
score = accuracy_score(labels_test,pred)
print ("ACCURACY IS ", score)
#########################################################


