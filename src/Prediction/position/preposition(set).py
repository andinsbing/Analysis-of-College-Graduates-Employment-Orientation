# -*- coding:UTF-8 -*-
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC,SVC
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import chi2,SelectKBest,SelectPercentile
from sklearn.model_selection import train_test_split
import numpy as np

data_label = pd.read_csv('data/lable',
                         header=None,
                         encoding='gbk')
data_feature = pd.read_csv('data/datanew',
                           header=None,
                           encoding='gbk')
# print(data_feature)
label = LabelEncoder()
target_doc = label.fit_transform(data_label)
data_feature = data_feature[0].apply(str)
vec = CountVectorizer(binary=True)
feature_doc = vec.fit_transform(data_feature)

vocabulary = vec.vocabulary_
# print(vocabulary)
var = VarianceThreshold()
feature_doc = var.fit_transform(feature_doc)
selector = SelectPercentile(chi2,50)
feature_doc = feature_doc[:5000]
target_doc = target_doc[:5000]
feature_array = feature_doc.toarray()
haha = {}

for item in feature_array:
    new=''
    for x in item:
        new+=str(x)
    if new in haha.keys():
        haha[new]+=1
    else:
        haha[new] = 1
# print(haha)

feature_doc = selector.fit_transform(feature_doc,target_doc)
train_x,test_x,train_y,test_y = train_test_split(feature_doc,target_doc,test_size=0.9)

clf4 = LogisticRegression(C=20.0,class_weight='balanced')
clf4.fit(train_x,train_y)
preds = clf4.predict(test_x)
print(classification_report(test_y,preds,digits=4))

test_x = vec.inverse_transform(test_x)
preds = label.inverse_transform(preds)
test_y = label.inverse_transform(test_y)
power = []
for item in test_x:
    str = ','.join(item)
    power.append(str)
data = pd.DataFrame(power)
data.columns = ['能力']
data['预测职业'] = pd.DataFrame(preds)
data['真实职业'] = pd.DataFrame(test_y)
data[['能力','预测职业','真实职业']].to_csv('positionresult.csv',index=None)
# data[['x','y_preds','y_true']].to_csv('positionresult.csv',index=None)
# print(power)
# print(preds)


