import uvicorn
from fastapi import FastAPI
from model import Model
from probabilityCalculater import ProbabilityCalculater

app = FastAPI()

@app.get("/{path}")
async def root(path):
    split_path = list(path.split("."))
    dict = {}
    count = 0
    for item in model.columns_to_work_on(model.classifier):
        dict[str(item)] = split_path[count]
        count += 1
    return probable.probability(dict)


if __name__ == '__main__':
    model = Model("computer_customers.csv",'Buy_Computer','id')
    probable = ProbabilityCalculater(model)
    uvicorn.run(app,host='127.0.0.1',port=8000)