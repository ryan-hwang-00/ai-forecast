from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

dic = {1: {'백산수2.0L': {'promotion': 'promotion_flag_1_bac_2',
                       'sale': 'sale_qty_1_bac_2'}
           }, {'백산수500ml': {'promotion': 'promotion_flag',
                            'sale': 'sale_qty_1_bac_5'}
               }, {'신라면멀티': {'promotion': 'promotion_flag_1_sin',
                             'sale': 'sale_qty_1_sin'}
                   }, {'안성탕면멀티': {'promotion': 'promotion_flag_1_ans',
                                  'sale': 'sale_qty_1_ans'}
                       }, {'진라면멀티(순한맛)': {'promotion': 'promotion_flag_1_jin',
                                          'sale': 'sale_qty_1_jin'}
                           },
       6: {'백산수2.0L': {'promotion': 'promotion_flag_6_bac_2',
                       'sale': 'sale_qty_6_bac_2'}
           }, {'백산수500ml': {'promotion': 'promotion_flag_6_bac_5', 'sale': 'sale_qty_6_bac_5'}
               }, {'신라면멀티': {'promotion': 'promotion_flag_6_sin', 'sale': 'sale_qty_6_sin'}
                   }, {'안성탕면멀티': {'promotion': 'promotion_flag_6_ans', 'sale': 'sale_qty_6_ans'}
                       }, {'진라면멀티(순한맛)': {'promotion': 'promotion_flag_6_jin', 'sale': 'sale_qty_6_jin'}
                           }}

app = Flask(__name__)
CORS(app)


@app.route("/api/v1.0/forecast/sale", methods=['POST'])
def predict():
    horizon = int(request.json['horizon'])

    future2 = m2.make_future_dataframe(periods=horizon)
    forecast2 = m2.predict(future2)

    data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:]
    # data = forecast2[['ds', 'yhat']][-horizon:]

    ret = data.to_json(orient='records', date_format='iso')

    return ret


# running REST interface, port=3000 for direct test
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=3000)
