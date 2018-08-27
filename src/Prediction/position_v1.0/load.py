# -*- coding:UTF-8 -*-
import pandas as pd
from sklearn.externals import joblib

# data_label = pd.read_csv('data/label_test',
#                          header=None,
#                          encoding='utf-8')
data_feature = pd.read_csv('data/datanew_test',
                           header=None,
                           encoding='utf-8')

clf = joblib.load('train_model.m')
label = joblib.load('label.l')
vec = joblib.load('vec.v')
var = joblib.load('var.v')
selector = joblib.load('selector.s')
data_feature = data_feature[0].apply(str)

feature_doc = vec.transform(data_feature)
feature_doc = var.transform(feature_doc)
feature_doc = selector.transform(feature_doc)
preds = clf.predict(feature_doc)
preds = label.inverse_transform(preds)
print(preds)

