from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from chatbot_helper import *

app = FastAPI()
# uvicorn main:app --reload
# ngrok http 8000
# tunnel non-temporaire ? https://sawfly-wanted-constantly.ngrok-free.app
@app.post('/')

async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if check_if_presentation_product(intent):
        product_tmp = get_product_name(intent)

    if intent=='check.coordinates':
        fulfillmentText = check_coordinates(parameters)
        return JSONResponse(content={
            'fulfillmentText': fulfillmentText
        })

    