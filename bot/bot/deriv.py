from deriv_api import DerivAPI
import websockets
import json

#app_id = 34800
app_id = 16014
#endpoint = 'blue.binaryws.com'
api_token_fake = '7wqh30BJvjjLDMN'
api_token_real = 'bThZrQNGmGxelJG'

async def login(accountType):
    #api = DerivAPI(endpoint='ws://{}'.format(endpoint), app_id=app_id)
    connection = await websockets.connect('wss://ws.binaryws.com/websockets/v3?app_id=16014')
    api = DerivAPI(connection=connection)

    if accountType == 'real':
        token = api_token_real
    else:
        token = api_token_fake
    authorize = await api.authorize(token)
    return authorize["authorize"]

async def logout():
    connection = await websockets.connect('wss://ws.binaryws.com/websockets/v3?app_id=16014')
    api = DerivAPI(connection=connection)
    api.logout()

async def getCache():
    connection = await websockets.connect('wss://ws.binaryws.com/websockets/v3?app_id=16014')
    api = DerivAPI(connection=connection)
    cache = await api.cache.authorize(api_token_fake)
    return cache