from fastapi import FastAPI

app = FastAPI(
    title="Demo FastAPI App",
    description="A simple FastAPI app to demonstrate GitHub Actions",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
