from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from bdd_helper import *

app = FastAPI()
# uvicorn main:app --reload
# tunnel non-temporaire ? https://sawfly-wanted-constantly.ngrok-free.app
@app.post('/')

async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    print(f'============{intent}===========')
    if check_if_presentation_product(intent):
        product_tmp = get_product_name(intent)
        print(product_tmp)

    