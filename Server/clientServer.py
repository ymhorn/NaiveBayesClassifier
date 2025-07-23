import uvicorn
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/{path}")
async def root(path):
    list_from_model = requests.get("http://con1:8000").json()
    if list_from_model[2]:
        split_path = list(path.split("."))
        dict_path = {}
        count = 0
        options = []
        try:
            for k, v in list_from_model[0].items():
                options = list(v.keys())
            for option in options:
                dict_path[option] = split_path[count]
                count += 1
            final_dict = {}
            for keys in list_from_model[0]:
                num = 1
                for key, value in dict_path.items():
                    num *= list_from_model[0][keys][key][value]
                final_dict[keys] = num * list_from_model[1][keys]
            return max(final_dict, key=final_dict.get)
        except IndexError:
            pass
    else:
        return "Test did not pass"
if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=8080)


