from fastapi import FastAPI

app = FastAPI()

DB_PASSWORD = 'AbC8ndl'


@app.get("/")
def read_root():
    return {"message": "Hello, welcome to FastAPI DevSecOps CI/CD Project"}


@app.get("/item/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
