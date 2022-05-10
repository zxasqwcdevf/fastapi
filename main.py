import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

futures = [...]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))