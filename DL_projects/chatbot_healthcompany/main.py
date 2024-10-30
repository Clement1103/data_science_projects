from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db_helper import *
from chatbot_helper import *

app = FastAPI()

# uvicorn main:app --reload
# ngrok http 8000
# tunnel non-temporaire ? https://sawfly-wanted-constantly.ngrok-free.app

sessions = {}

@app.post('/')
async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts'][0]['name']

    session_id = get_session_id(output_contexts)

    print('===', intent, '===')

    if session_id not in sessions:
        sessions[session_id] = {
            "product_tmp": None,
            "list_interests": []
        }

    user_session = sessions[session_id]

    if check_if_presentation_product(intent):
        user_session["product_tmp"] = get_product_name(intent)
        print("Produit capté :", user_session["product_tmp"])

    is_interested = check_interest(intent)
    print("IS INTERESTED: ", is_interested)
    print("PRODUCT TMP: ", user_session["product_tmp"])

    if is_interested is True and user_session["product_tmp"]:
        user_session["list_interests"].append(user_session["product_tmp"])
        user_session["product_tmp"] = ''

    print('====', user_session["list_interests"], '====')
    print('==========', user_session, '==========')


# @app.post('/')
# async def handle_request(request: Request):
    # payload = await request.json()
    # intent = payload['queryResult']['intent']['displayName']
    # parameters = payload['queryResult']['parameters']
    # output_contexts = payload['queryResult']['outputContexts'][0]['name']
    # product_tmp =''
    # print('===',intent,'===')
    # session_id = get_session_id(output_contexts)
    # if check_if_presentation_product(intent):
    #     product_tmp = get_product_name(intent)
    #
    # if check_interest(intent):
    #     # print(intent) js
    #     list_interests.append(product_tmp)
    #     product_tmp=''
    #
    # print('====',list_interests, '====')
    # if intent=='check.coordinates':
    #     fulfillmentText = check_coordinates(parameters)
    #     return JSONResponse(content={
    #         'fulfillmentText': fulfillmentText
    #     })
# async def handle_request(request: Request):
#     payload = await request.json()
#     intent = payload['queryResult']['intent']['displayName']
#     parameters = payload['queryResult']['parameters']
#     output_contexts = payload['queryResult']['outputContexts'][0]['name']
#
#     print('===', intent, '===')
#
#     # Obtenir l'ID de session
#     session_id = get_session_id(output_contexts)
#
#     # Vérifier si l'intent est une présentation de produit et obtenir le nom du produit
#     if check_if_presentation_product(intent):
#         product_tmp = get_product_name(intent)
#         print(product_tmp)
#     # Vérifier l'intérêt et mettre à jour list_interests si le client est intéressé
#     is_interested = check_interest(intent)
#     print("IS INTERESTED: ", is_interested)
#     print("PRODUCT TMP: ", product_tmp)
#     if is_interested is True and product_tmp:
#         list_interests.append(product_tmp)
#         product_tmp = ''  # Réinitialiser product_tmp après l'ajout
#
#     print('====', list_interests, '====')
