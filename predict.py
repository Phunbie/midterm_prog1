from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import pickle

col=['basket_icon_click','basket_add_list','basket_add_detail','sort_by','image_picker',
 'account_page_click','promo_banner_click','detail_wishlist_add','list_size_dropdown',
 'closed_minibasket_click','checked_delivery_detail','checked_returns_detail','sign_in',
 'saw_checkout','saw_sizecharts','saw_delivery','saw_account_upgrade','saw_homepage','device_mobile',
 'device_computer','device_tablet','returning_user','loc_uk']


def load(filename):
     with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


model = load('model_logistic.bin')

app = Flask('propensity')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    cat = pd.DataFrame([customer])
    X = cat[col]

    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'propensity_probability': float(y_pred),
        'propensity to purchase': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8181)



