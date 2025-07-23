import numpy as np
import pandas as pd

class Model:
    def __init__(self,path,classifier,drop_columns = None):
        self.classifier = classifier
        self.DF = pd.read_csv(path)
        if drop_columns:
            self.DF.drop(drop_columns,axis=1,inplace=True)

    @staticmethod
    def unique_values(dataframe,column):
        return dataframe[column].unique()

    @staticmethod
    def amount_of_unique_values(dataframe,column,value):
        return float(dataframe.loc[dataframe[column] == value,column].count())

    @staticmethod
    def amount_of_all_values(dataframe):
        return float(dataframe.shape[0])

    def split_dataframe_by_value(self,column,value):
        return self.DF.groupby(column).get_group(value)

    def columns_to_work_on(self,classifier):
        columns = self.DF.columns
        return columns.drop(classifier)

    @staticmethod
    def change_numpy_ints(item):
        if isinstance(item,np.generic):
            return int(item)
        elif isinstance(item,dict):
            return {Model.change_numpy_ints(k): Model.change_numpy_ints(v) for k, v in item.items()}
        else:
            return item

    def dict_class(self):
        class_dict = {}
        all_values = self.amount_of_all_values(self.DF)
        for val in self.unique_values(self.DF,self.classifier):
            unique_values = self.amount_of_unique_values(self.DF,self.classifier,val)
            class_dict[val] = unique_values / all_values
        class_dict = self.change_numpy_ints(class_dict)
        return class_dict

    def dict_values(self):
        dict1 = {}
        for val in self.unique_values(self.DF,self.classifier):
            split_df = self.split_dataframe_by_value(self.classifier,val)
            column = self.columns_to_work_on(self.classifier)
            dict2 = {}
            for col in column:
                count_val = self.amount_of_all_values(split_df)
                unique_val = self.unique_values(self.DF,col)
                split_unique_val = self.unique_values(split_df,col)
                dict3 = {}
                if len(unique_val) == len(split_unique_val):
                    for value in unique_val:
                        value_count = self.amount_of_unique_values(split_df,col,value)
                        dict3[value] = value_count / count_val
                else:
                    count_val += len(unique_val)
                    for value in unique_val:
                        value_count = self.amount_of_unique_values(split_df, col, value) + 1
                        dict3[value] = value_count / count_val
                dict2[col] = dict3
            dict1[val] = dict2
        final = self.change_numpy_ints(dict1)
        return final
