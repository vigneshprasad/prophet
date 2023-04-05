from flask import Flask, request, jsonify
import pandas as pd
from prophet import Prophet

app = Flask(__name__)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome API!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "No name found. Please send a name."
        })


@app.route('/')
def index():
    # A welcome message to test our server
    df = pd.read_csv('data.csv')
    df['cap'] = 8.5

    df.head()

    m = Prophet()
    m.fit(df)

    future = m.make_future_dataframe(periods=10, freq='W')
    fcst = m.predict(future)
    fcst.to_csv('PredictOutput.csv')
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)