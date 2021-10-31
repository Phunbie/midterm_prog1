import requests
import json
customer={"UserID":"a0c0-6b73247c-a0c0-4bd9-8baa-797356",
 "basket_icon_click":0,
 "basket_add_list":0,
 "basket_add_detail":1,
 "sort_by":0,
 "image_picker":0,
 "account_page_click":1,
 "promo_banner_click":1,
 "detail_wishlist_add":0,
 "list_size_dropdown":1,
 "closed_minibasket_click":0,
 "checked_delivery_detail":1,
 "checked_returns_detail":0,
 "sign_in":0,
 "saw_checkout":0,
 "saw_sizecharts":0,
 "saw_delivery":0,
 "saw_account_upgrade":0,
 "saw_homepage":0,
 "device_mobile":0,
 "device_computer":0,
 "device_tablet":0,
 "returning_user":1,
 "loc_uk":1}

url = 'http://localhost:8181/predict'
response = requests.post(url, json=customer)
result = response.json()

print(json.dumps(result, indent=2))