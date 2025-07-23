from probabilityCalculater import ProbabilityCalculater

class Tester:
    def __init__(self,original_model):
        self.model = original_model

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
        probable = ProbabilityCalculater(self.model)
        for k,v in self.data_frame_to_dict(trial_data.drop(self.model.classifier,axis=1)).items():
            if str(probable.probability(v)) == str(trial_data.loc[k,self.model.classifier]):
                right += 1
            else:
                wrong += 1
        return right / (right + wrong)





