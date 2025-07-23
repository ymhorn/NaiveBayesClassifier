import uvicorn
from fastapi import FastAPI
from ModelBuilder.model import Model
from ModelBuilder.probabilityCalculater import ProbabilityCalculater
from ModelBuilder.tester import Tester

app = FastAPI()

# @app.get("/model")
# async def root():
#     model = Model("phishing.csv", 'class', 'Index')
#     return str(model.dict_values())

@app.get("/")
async def root():
    model = Model("phishing.csv", 'class', 'Index')
    test = Tester(model)
    if test.test() > 0.9:
        return [model.dict_values(),model.dict_class(),True]
    else:
        return [model.dict_values(),model.dict_class(),False]

@app.get("/{path}")
async def root(path,list_from_model):
    split_path = list(path.split("."))
    dict_path = {}
    count = 0
    a = []
    for k , v  in list_from_model[0].items():
        a = list(v.keys)
    for b in a:
        dict_path[b] = split_path[count]
        count += 1
    final_dict = {}
    for keys in list_from_model[0]:
        num = 1
        for key, value in dict_path.items():
            num *= list_from_model[0][keys][key][value]
        final_dict[keys] = num * list_from_model[1][keys]
    return max(final_dict, key=final_dict.get)






@app.get("/{path}")
async def root(path):
    model = Model("phishing.csv", 'class', 'Index')
    probable = ProbabilityCalculater(model)
    test = Tester(model)
    if test.test() > 0.5:
        split_path = list(path.split("."))
        dict = {}
        count = 0
        try:
            for item in model.columns_to_work_on(model.classifier):
                try:
                    num = int(split_path[count])
                    dict[item] = num
                except ValueError:
                    dict[item] = split_path[count]
                finally:
                    count += 1
            try:
                return int(probable.probability(dict))
            except ValueError:
                return probable.probability(dict)
        except IndexError:
            pass
    elif test.test() < 0.5:
        return "The test did not pass"
    else:
        return "duh"
    # except KeyError:
    #     count = 0
    #     split = [int(a) for a in split_path]
    #     for item in model.columns_to_work_on(model.classifier):
    #         dict[item] = split[count]
    #         count += 1
    #     return int(probable.probability(dict))
    # except IndexError:
    #     pass


if __name__ == '__main__':
    # model = Model("computer_customers.csv",'BC','id')
    # probable = ProbabilityCalculater(model)
    uvicorn.run(app,host='127.0.0.1',port=8000)