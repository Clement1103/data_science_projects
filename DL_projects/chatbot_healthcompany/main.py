from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
# uvicorn main:app --reload
# tunnel non-temporaire ? https://sawfly-wanted-constantly.ngrok-free.app
@app.post('/')

async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    