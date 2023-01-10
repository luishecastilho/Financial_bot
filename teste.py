from deriv_api import DerivAPI
import asyncio

#app_id = 34800
app_id = 16014
endpoint = 'blue.binaryws.com'
#api_token = 'a1-gTocLCPtr4P7BJbj4aFLbB2JeNj9T'

async def login():
    print('oi')

    api = DerivAPI(endpoint='ws://{}'.format(endpoint), app_id=app_id)
    print('deu')

asyncio.run(login())