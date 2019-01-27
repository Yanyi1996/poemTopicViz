"""
classification of real and fake news using logistic regression
    - data split 80%
    - optimize with IDF weights and bi-grams
"""
import os, re
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.linear_model import LogisticRegressionCV

root = 'I:\\AU summer school 2017\\text mining the great unread\\day 7'
filepath = os.path.join(root,'fake_or_real_news.dat')
os.chdir(root)

# import data
data = pd.read_csv(filepath)

# print classes
print(set(data.label))
print('number of fake news texts:', sum(data['label'] == 'FAKE'))

# inspect classes
print(data.label.value_counts())

# clean df by removing non-alphabetic chars
text_clean = []
for text in data['text']:
    text = re.sub(r'[^a-zA-Z]',' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.rstrip()
    text_clean.append(text)
    
# add clean text to df
data['text_clean'] = text_clean

# split data
ratio = 0.8
mask = np.random.rand(len(data)) < ratio
data_train = data[mask]
data_test = data[~mask]

# control size of data sets 
print(len(data_train)/len(data))
print(len(data_test.shape)/len(data))

# divide data sets in features X and class y
train_X = data_train['text_clean'].values # features
train_y = data_train['label'].values # classes

# testing/validation
test_X = data_test['text_clean'].values # features
test_y = data_test['label'].values # classes

# minimal pipeline for sklearn training
vecspc = CountVectorizer() # instantiate vectorizer
vecspc = TfidfVectorizer() # instantiate TF-IDF vectorizer
vecspc = CountVectorizer(ngram_range = (1,2)) # also count bigrams, but take long time

train_feat = vecspc.fit_transform(train_X)

# inspecting feature names
feat_names = vecspc.get_feature_names()
print(len(feat_names))

# train the classifier
clf = LogisticRegressionCV() # instantiate classifier
clf.fit(train_feat, train_y)

# optional: saving your classifier
import pickle
with open('class_logreg_fake.pcl', 'wb') as file_object:
    pickle.dump(clf, file_object)

# import pickled classifier
clf = pickle.load(open('class_logreg_fake.pcl', 'rb'))

# VALIDATION
test_feat = vecspc.transform(test_X)
pred = clf.predict(test_feat)

# performance metrics
# confusion matrix
conf_mat = metrics.confusion_matrix(test_y, pred)
print(conf_mat)
perf_acc = metrics.accuracy_score(test_y, pred)
print(perf_acc)

# standard performance metric
perf_f1 = metrics.f1_score(test_y, pred, pos_label = 'REAL')
print(perf_f1)
print(metrics.classification_report(test_y, pred))

# exploring features and document classification
import eli5 # need to download this module

# most information features
eli5.show_weights(clf, vec = vecspc, top = 25)

# explore document
i = 2
text = data['text_clean'][i]
print(data.label[i])







   


















    

