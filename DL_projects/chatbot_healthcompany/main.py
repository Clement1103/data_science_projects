from fastapi import FastAPI

app = FastAPI()
# uvicorn main:app --reload
# tunnel non-temporaire ? https://sawfly-wanted-constantly.ngrok-free.app
@app.get('/')

async def root():
    return {'message': 'Hello World'}