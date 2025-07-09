from typing import final

import pandas as pd
from pprint import pprint


# computer_buyers = pd.read_csv('computer_customers.csv',index_col='id')
# computer_buyers.sort_index(inplace=True)
# split = computer_buyers.groupby('Buy_Computer').get_group('yes')
# print(split)

class NaiveBayes:
    def __init__(self,path,classifier,drop_columns):
        self.path = path
        self.classifier = classifier
        self.DB = pd.read_csv(self.path)
        self.DB.drop(drop_columns,axis=1,inplace=True)

    def create_dict_class(self):
        class_dict = {}
        unique_class = self.DB[self.classifier].unique()
        for val in unique_class:
            class_dict[val] = float(self.DB.loc[self.DB[self.classifier] == val,self.classifier].count() / self.DB[self.classifier].count())
        return class_dict

    def create_dict_values(self):
        unique_class = self.DB[self.classifier].unique()
        dict1 = {}
        for val in unique_class:
            split_df = self.DB.groupby(self.classifier).get_group(val)
            column = self.DB.columns
            column = column.drop(self.classifier)
            dict2 = {}
            for col in column:
                count_val = split_df[self.classifier].count()
                unique_val = self.DB[col].unique()
                split_unique_val = split_df[col].unique()
                dict3 = {}
                if len(unique_val) == len(split_unique_val):
                    for value in unique_val:
                        dict3[value] = float(split_df.loc[split_df[col] == value,col].count() / count_val)
                else:
                    count_val += len(unique_val)
                    for value in unique_val:
                        dict3[value] = float((split_df.loc[split_df[col] == value, col].count() +1) / count_val)
                dict2[col] = dict3
            dict1[val] = dict2
        return dict1

    def input(self):
        column_options = list(self.create_dict_values().values())[0]
        input_dict = {}
        for k,v in column_options.items():
            options = dict(enumerate(list(v.keys())))
            choice = input(f"{k}:\n {options}\n")
            if int(choice) in options.keys():
                input_dict[k] = options[int(choice)]
            else:
                print("Not a valid option please start again")
                return self.input()
        return input_dict

    def result(self,input_dictionary):
        final_dict = {}
        for keys in self.create_dict_values():
            num = 1
            for key,value in input_dictionary.items():
                num *= self.create_dict_values()[keys][key][value]
            final_dict[keys] = num * self.create_dict_class()[keys]
        print(final_dict)
        return max(final_dict,key=final_dict.get)





a = NaiveBayes('computer_customers.csv','Buy_Computer','id')
pprint(a.result(a.input()))

