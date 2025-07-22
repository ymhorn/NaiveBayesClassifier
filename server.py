from os.path import split

import uvicorn
from fastapi import FastAPI
from model import Model
from probabilityCalculater import ProbabilityCalculater

app = FastAPI()

@app.get("/{path}")
async def root(path):
    model = Model("computer_customers.csv", 'BC', 'id')
    probable = ProbabilityCalculater(model)
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