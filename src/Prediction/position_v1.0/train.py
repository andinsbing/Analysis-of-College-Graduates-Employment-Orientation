# -*- coding:UTF-8 -*-
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import chi2,SelectPercentile

data_label = pd.read_csv('data/lable',
                         header=None,
                         encoding='gbk')
data_feature = pd.read_csv('data/datanew',
                           header=None,
                           encoding='gbk')
label = LabelEncoder()
# print(data_label)
target_doc = label.fit_transform(data_label)
# print(target_doc)
data_feature = data_feature[0].apply(str)
vec = CountVectorizer(binary=True)
feature_doc = vec.fit_transform(data_feature)
# print(feature_doc)
# vocabulary = vec.vocabulary_
feature_array = feature_doc.toarray()

var = VarianceThreshold()
feature_doc = var.fit_transform(feature_doc)

selector = SelectPercentile(chi2,50)
feature_doc = selector.fit_transform(feature_doc,target_doc)

clf4 = LogisticRegression(C=20.0,class_weight='balanced')
clf4.fit(feature_doc,target_doc)

joblib.dump(clf4,'train_model.m')
joblib.dump(vec,'vec.v')
joblib.dump(label,'label.l')
joblib.dump(var,'var.v')
joblib.dump(selector,'selector.s')
