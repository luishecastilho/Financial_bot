from deriv_api import DerivAPI
import websockets
import json

#app_id = 34800
app_id = 16014
#endpoint = 'blue.binaryws.com'
api_token = '7wqh30BJvjjLDMN'

async def login():
    #api = DerivAPI(endpoint='ws://{}'.format(endpoint), app_id=app_id)
    connection = await websockets.connect('wss://ws.binaryws.com/websockets/v3?app_id=16014')
    api = DerivAPI(connection=connection)
    authorize = await api.authorize(api_token)
    
    return authorize["authorize"]