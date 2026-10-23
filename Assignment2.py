from fastapi import FastAPI

app = FastAPI()

@app.post("/add")
def add(num1, num2):
    total =  int(num1)+int(num2)
    return {"sum": total}
