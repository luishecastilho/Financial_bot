from deriv_api import DerivAPI
import websockets
import json

#app_id = 34800
app_id = 16014
#endpoint = 'blue.binaryws.com'
api_token_fake = '7wqh30BJvjjLDMN'
api_token_real = 'bThZrQNGmGxelJG'

async def authorize(token=api_token_real):
    #api = DerivAPI(endpoint='ws://{}'.format(endpoint), app_id=app_id)
    #connection = await websockets.connect('wss://ws.binaryws.com/websockets/v3?app_id=16014')
    api = DerivAPI(app_id=16014)

    authorize = await api.authorize('7wqh30BJvjjLDMN')
    print(authorize["authorize"])
    return authorize["authorize"]
    
"""
async def logout():
    connection = await websockets.connect('wss://ws.binaryws.com/websockets/v3?app_id=16014')
    api = DerivAPI(connection=connection)
    api.logout()
    """

async def getCache():
    connection = await websockets.connect('wss://ws.binaryws.com/websockets/v3?app_id=16014')
    api = DerivAPI(connection=connection)
    cache = await api.cache.authorize(api_token_fake)
    return cache