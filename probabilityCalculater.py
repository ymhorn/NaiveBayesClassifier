import pandas as pd
from pprint import pprint
from model import Model

class ProbabilityCalculater:
    def __init__(self,model):
        self.model = model
        self.dict_values = self.model.dict_values()
        self.dict_class_values = self.model.dict_class()

    def probability(self,input_dict):
        final_dict = {}
        for keys in self.dict_values:
            num = 1
            for key, value in input_dict.items():
                num *= self.dict_values[keys][key][value]
            final_dict[keys] = num * self.dict_class_values[keys]
        return max(final_dict,key=final_dict.get)
