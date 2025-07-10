from model import Model
from probabilityCalculater import ProbabilityCalculater



class UserInput:
    def __init__(self,model):
        self.model = model
        self.dict_values = self.model.dict_values()

    def create_dict(self):
        column_options = list(self.dict_values.values())[0]
        input_dict = {}
        for k, v in column_options.items():
            options = dict(enumerate(list(v.keys())))
            choice = input(f"{k}:\n {options}\n")
            if int(choice) in options.keys():
                input_dict[k] = options[int(choice)]
            else:
                print("Not a valid option please start again")
                return self.create_dict()
        return input_dict

    def probability(self):
        calculate = ProbabilityCalculater(self.model)
        return calculate.probability(self.create_dict())

# a = Model('computer_customers.csv','Buy_Computer','id')
# b = UserInput(a)
# print(b.probability())