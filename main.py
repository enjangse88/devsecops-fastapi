from fastapi import FastAPI

app = FastAPI()

SECRET_KEY = "Abcndkdm34"

@app.get("/")
def read_root():
    return {"message": "Hello, welcome to FastAPI DevSecOps CI/CD Project"}


@app.get("/item/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
