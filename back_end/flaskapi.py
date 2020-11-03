from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

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
