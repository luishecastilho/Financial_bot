from deriv_api import DerivAPI
from deriv_api import APIError


app_id = 34800
api_token = 'a1-gTocLCPtr4P7BJbj4aFLbB2JeNj9T'

async def sample_calls():
    api = DerivAPI(app_id=app_id)


    response = await api.ping({'ping': 1})
    if response['ping']:
        print(response['ping'])

    #active_symbols = await api.active_symbols({"active_symbols": "brief", "product_type": "basic"})
    #print(active_symbols)

    # Authorize
    #authorize = await api.authorize(api_token)
    #print(authorize)

    # Get Balance
    #response = await api.balance()
    #print(response)