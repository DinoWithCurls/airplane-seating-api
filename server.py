from flask import Flask, jsonify, request

from airplane import airplane_seating

app = Flask(__name__)

@app.route('/airplane-algo', methods=["POST"])
def process():
    content = request.json
    seatsGrid = content["seatsGrid"]
    passengers = content["passengers"]
    result = {}
    seating_arrangement = airplane_seating(seatsGrid, passengers)
    result = {"arrangement": seating_arrangement}
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)