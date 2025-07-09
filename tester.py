import pandas as pd
from pprint import pprint
from model import Model
from probabilityCalculater import ProbabilityCalculater

class Tester:
    def __init__(self,model):
        self.model = model

    def sample(self,fraction):
        return self.model.DF.sample(frac=fraction)

    @staticmethod
    def left_sample(sample,original):
        return original[~original.index.isin(sample.index)]

    @staticmethod
    def data_frame_to_dict(dataframe):
        return dataframe.to_dict('index')

    def test(self):
        right = 0
        wrong = 0
        test_sample = self.sample(0.7)
        original_dataframe = self.model.DF
        self.model.DF = test_sample
        trial_data = self.left_sample(test_sample,original_dataframe)
        for k,v in self.data_frame_to_dict(trial_data.drop(self.model.classifier,axis=1)).items():
            probable = ProbabilityCalculater(self.model,v)
            if probable.probability() == str(trial_data.loc[k,self.model.classifier]):
                right += 1
            else:
                wrong += 1
        return right / (right + wrong)


model = Model('computer_customers.csv','Buy_Computer','id')

tester = Tester(model)

print(tester.test())




