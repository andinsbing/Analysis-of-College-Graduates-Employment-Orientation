# -*- coding:UTF-8 -*-
import pandas as pd
from sklearn.externals import joblib

class positionPre:
    def __init__(self):
        self.__clf = joblib.load('train_model.m')
        self.__label = joblib.load('label.l')
        self.__vec = joblib.load('vec.v')
        self.__var = joblib.load('var.v')
        self.__selector = joblib.load('selector.s')
    def _pred(self,data_feature):
        feature_doc = self.__vec.transform(data_feature)
        feature_doc = self.__var.transform(feature_doc)
        feature_doc = self.__selector.transform(feature_doc)
        preds = self.__clf.predict(feature_doc)
        preds = self.__label.inverse_transform(preds)
        result = preds.tolist()
        return str(result[0])
    def CSV_Pre(self,path):
        try:
            data_feature = pd.read_csv(path,
                        header=None,
                        encoding='utf-8')
        except : print('CSV文件打开失败！')
        data_feature = data_feature[0].apply(str)
        return self._pred(data_feature)
    def Str_Pre(self,string):
        data_feature = pd.Series(string)
        data_feature = data_feature.apply(str)
        return self._pred(data_feature)
    def List_Pre(self,lists):
        res_list = []
        for f_str in lists:
            res_list.append(self.Str_Pre(f_str))
        return res_list

#示例
position = positionPre()
print(position.Str_Pre('上进心 外语基础 文案能力 团队协作能力 专业素质良好 设计能力 学习能力'))
print(position.CSV_Pre('data/datanew_test'))
print(position.List_Pre(list(['上进心 外语基础 文案能力','团队协作能力 专业素质良好 设计能力 学习能力'])))


