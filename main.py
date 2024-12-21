import uvicorn
from fastapi import FastAPI, Path, Response
from typing import Annotated

app = FastAPI()

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response:Response):
 response.headers[name] = value
 return "normal body"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
