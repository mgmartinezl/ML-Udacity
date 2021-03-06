#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
import sklearn
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
def classify(features_train, labels_train):
    from sklearn.naive_bayes import GaussianNB
    t0 = time()
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    print("training time:", round(time() - t0, 3), "s")
    return clf

naive_bayes = classify(features_train, labels_train)
t0 = time()
email_pred_test = naive_bayes.predict(features_test)
print("prediction time:", round(time() - t0, 3), "s")

acc_test = sklearn.metrics.accuracy_score(labels_test, email_pred_test)
print(acc_test)

#########################################################


