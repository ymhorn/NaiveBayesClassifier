import pandas as pd


# computer_buyers = pd.read_csv('computer_customers.csv',index_col='id')
# computer_buyers.sort_index(inplace=True)
# split = computer_buyers.groupby('Buy_Computer').get_group('yes')
# print(split)

class NaiveBayes:
    def __init__(self,path,classifier):
        self.path = path
        self.classifier = classifier
        self.DB = pd.read_csv(self.path)

    def create_dict_class(self):
        class_dict = {}
        unique_class = self.DB[self.classifier].unique()
        for val in unique_class:
            class_dict[val] = float(self.DB.loc[self.DB[self.classifier] == val,self.classifier].count() / self.DB[self.classifier].count())
        return class_dict

    def create_dict_values(self):
        dict1 = {}
        unique_class = self.DB[self.classifier].unique()
        for val in unique_class:
            split_df = self.DB.groupby(self.classifier).get_group(val)
            count_val = split_df[self.classifier].count()
            dict2 = {}
            column = self.DB.columns[1:]
            for col in column:
                unique_val = self.DB[col].unique()
                dict3 = {}
                for value in unique_val:
                    dict3[value] = float(split_df.loc[split_df[col] == value,col].count() / count_val)
                dict2[col] = dict3
            dict1[val] = dict2
        return dict1





a = NaiveBayes('computer_customers.csv','Buy_Computer')
print(a.create_dict_values())