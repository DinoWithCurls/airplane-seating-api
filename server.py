from flask import Flask, jsonify, request
#from flask_cors import cross_origin
from flask_cors import CORS
from airplane import airplane_seating

app = Flask(__name__)

CORS(app)

@app.route('/airplane-algo', methods=["POST"])
#@cross_origin()
def process():
    content = request.json
    seatsGrid = content["seatsGrid"]
    passengers = content["passengers"]
    seating_arrangement = airplane_seating(seatsGrid, passengers)
    result = {"arrangement": seating_arrangement}
    response = jsonify(result)
    response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:3000")
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)