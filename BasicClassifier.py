import pandas as pd
from pprint import pprint

# computer_buyers = pd.read_csv('computer_customers.csv',index_col='id')
# computer_buyers.sort_index(inplace=True)
# split = computer_buyers.groupby('Buy_Computer').get_group('yes')
# print(split)

class NaiveBayes:
    def __init__(self,path,classifier,drop_columns):
        self.classifier = classifier
        self.DF = pd.read_csv(path)
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

    def sample(self,fraction):
        return self.DF.sample(frac=fraction)

    def left_sample(self,sample):
        return self.DF[~self.DF.index.isin(sample.index)]

    def create_dict_class(self):
        class_dict = {}
        all_values = self.amount_of_all_values(self.DF)
        for val in self.unique_values(self.DF,self.classifier):
            unique_values = self.amount_of_unique_values(self.DF,self.classifier,val)
            class_dict[val] = unique_values / all_values
        return class_dict

    def create_dict_values(self):
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

    def test(self):
        sample = self.sample(0.7)
        to_sample_with = self.left_sample(sample)







a = NaiveBayes('computer_customers.csv','Buy_Computer','id')
pprint(a.test())

