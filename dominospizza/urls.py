_dominos_api_base_url = 'https://order.dominos.com/power/'
_dominos_tracker_base_url = 'https://trkweb.dominos.com/orderstorage/GetTrackerData?'

# self.locator = DOMINOS_API_BASE_URL + 'store-locator?s={street_name}&c={zip_code}'
# self.profile = DOMINOS_API_BASE_URL + 'store/{store_id}/profile'
# self.menu = DOMINOS_API_BASE_URL + 'store/{store_id}/menu?lang={lang}&structured=true'

# self.validate_order = DOMINOS_API_BASE_URL + 'validate-order'
# self.price_order = DOMINOS_API_BASE_URL + 'price-order'
# self.place_order = DOMINOS_API_BASE_URL + 'place-order'

def store_locator_url():
    return _dominos_api_base_url + 'store-locator'

def store_information_url(store_id):
    return _dominos_api_base_url + 'store/{s}/profile'.format(s=store_id)

def store_menu_url(store_id):
    return _dominos_api_base_url + 'store/{s}/menu?lang={l}&structured=true'.format(s=store_id,l='en')

def validate_order_url():
    return _dominos_api_base_url + 'validate-order'

def price_order_url():
    return _dominos_api_base_url + 'price-order'

def palce_order_url(zip_code, street_name):
    return _dominos_api_base_url + 'place-order'
