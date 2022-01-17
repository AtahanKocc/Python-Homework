
"""
Author: Atahan Koç
Description Part: In this question, we were given Breast Cancer Dataset, we were asked to develop SVM and Naive Bayes classifier for this given classification problem.
Instructions and codes on how to develop it were included in the assignment. After reviewing these instructions and the code, i solved the problem by following these instructions and got the output.
In addition, the answers to the questions given in the homework were explained verbally in the Output section.
"""

import numpy as np
import matplotlib.pyplot as plt

# I load the cancer dataset
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = data.data # Input features
y = data.target # Class label (0: Malignant, 1: Benign)

# Now, i separate your data types of 70% training and 30% test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
y_train = np.reshape(y_train, (-1,1))
y_test = np.reshape(y_test, (-1,1))

# I added scikit-learn library has built-in methods for Naive Bayes and SVM classification.
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
svm_cl = SVC(C=1, gamma='scale', probability=True)
bayes_cl = GaussianNB(var_smoothing=1e-7)

svm_cl.fit(X_train,y_train) # cl is classifier model to train
y_pred_svm = svm_cl.predict(X_test)
y_prob_svm = svm_cl.predict_proba(X_test)[:,1]

bayes_cl.fit(X_train,y_train)
y_pred_bayes = bayes_cl.predict(X_test)
y_prob_bayes = bayes_cl.predict_proba(X_test)[:,1]

from sklearn.metrics import accuracy_score, roc_curve, auc
# The prediction accuracy
print ("Prediction accuracy (SVM) : %.2f" % accuracy_score(y_test,y_pred_svm))
# Receiver Operating Cracateristic Curve (ROC)
fpr, tpr, thr = roc_curve(y_test, y_prob_svm)
plt.plot(fpr, tpr)

from sklearn.metrics import accuracy_score,roc_curve,auc
print("Prediction accuracy (bayes) : %.2f" % accuracy_score(y_test,y_pred_bayes))
fpr, tpr, thresholds = roc_curve(y_test, y_prob_bayes)
plt.plot(fpr,tpr)


"""
Output:
Prediction accuracy (svm) : 0.92
Prediction accuracy (bayes): 0.94
*********************************

Part A) 94 % Prediction accuracy (bayes)


Part B) Classifier parameters are responsible for determining the optimal parameters for the problem and optimizing the classifier's parameters, which is crucial in estimating the evaluation measure.


Part C) The Naive Bayes and SVM classifiers are both sensitive to parameter tuning. 
However, when compared to the Naive Bayes technique, SVM Classifiers provide better accuracy and faster estimates. 
One reason is that SVM is more likely to perform better since it can handle nonlinearities in the data.

Part D) Instead than measuring the absolute value of the estimations, AUC measures how well they rank. Regardless of which classification criterion is chosen, also AUC assesses the quality of the model's results.

"""

