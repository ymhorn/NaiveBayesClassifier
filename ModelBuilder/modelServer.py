import uvicorn
from fastapi import FastAPI
from model import Model
from probabilityCalculater import ProbabilityCalculater
from tester import Tester

app = FastAPI()

@app.get("/")
async def root():
    model = Model("phishing.csv", 'class', 'Index')
    test = Tester(model)
    passed = True
    if test.test() < 0.9:
        passed = False
    return [model.dict_values(),model.dict_class(),passed]

# @app.get("/{path}")
# async def root(path):
#     model = Model("phishing.csv", 'class', 'Index')
#     probable = ProbabilityCalculater(model)
#     test = Tester(model)
#     if test.test() > 0.5:
#         split_path = list(path.split("."))
#         dict = {}
#         count = 0
#         try:
#             for item in model.columns_to_work_on(model.classifier):
#                 try:
#                     num = int(split_path[count])
#                     dict[item] = num
#                 except ValueError:
#                     dict[item] = split_path[count]
#                 finally:
#                     count += 1
#             try:
#                 return int(probable.probability(dict))
#             except ValueError:
#                 return probable.probability(dict)
#         except IndexError:
#             pass
#     elif test.test() < 0.5:
#         return "The test did not pass"
#     else:
#         return "duh"


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)