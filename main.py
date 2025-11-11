from fastapi import FastAPI

app = FastAPI()


@app.get("/isEven/{num}")
async def root(num: int):
    return {"isEven": num % 2 == 0}
