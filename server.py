import uvicorn
from fastapi import FastAPI
from model import Model
from probabilityCalculater import ProbabilityCalculater

app = FastAPI()

@app.get("/{path}")
async def root(path):
    split_path = list(path.split("."))
    dict = {}
    try:
        count = 0
        for item in model.columns_to_work_on(model.classifier):
            dict[item] = split_path[count]
            count += 1
        return probable.probability(dict)
    except KeyError:
        count = 0
        split = [int(a) for a in split_path]
        for item in model.columns_to_work_on(model.classifier):
            dict[item] = split[count]
            count += 1
        return int(probable.probability(dict))
    except IndexError:
        pass


if __name__ == '__main__':
    model = Model("phishing.csv",'class','Index')
    probable = ProbabilityCalculater(model)
    uvicorn.run(app,host='127.0.0.1',port=8000)