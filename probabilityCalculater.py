import pandas as pd
from pprint import pprint
from model import Model

class ProbabilityCalculater:
    def __init__(self,model,input_dict):
        self.model = model
        self.input_dict = input_dict

    def probability(self):
        final_dict = {}
        for keys in self.model.dict_values():
            num = 1
            for key, value in self.input_dict.items():
                num *= self.model.dict_values()[keys][key][value]
            final_dict[keys] = num * self.model.dict_class()[keys]
        return max(final_dict,key=final_dict.get)
