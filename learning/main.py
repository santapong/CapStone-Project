from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def test():
    pass

if __name__ == '__main__':
    uvicorn.run('main:app', port=8001, reload=True)