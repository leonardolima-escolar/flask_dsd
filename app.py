from flask import Flask, request, jsonify
import requests
import db

app = Flask(__name__)


@app.route("/countries", methods=['GET'])
def get_countries():
    countries = db.query_db('select * from countries')
    return jsonify(countries), 200


@app.route("/countries", methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        id = db.insert((country['country_name'], country['capital']))
        return {"id": id}, 201
    return {"error": "Request must be JSON"}, 415


@app.route("/countries/<int:id>", methods=['GET'])
def get_country(id):
    country = db.query_db(
        f'select * from countries where countries.id={id}')
    return jsonify(country), 200


@app.route("/countries/<int:id>", methods=['PUT'])
def edit_country(id):
    if request.is_json:
        country = request.get_json()
        id = db.edit((country['country_name'],
                     country['capital'], id))
        return {"id": id}, 201
    return {"error": "Request must be JSON"}, 415


@app.route("/countries/<int:id>", methods=['DELETE'])
def delete_country(id):
    d = db.query_db(
        f'delete from countries where countries.id={id}')
    return jsonify(d), 200


if __name__ == '__main__':
    init_db = False

    db.init_app(app)

    if init_db:
        with app.app_context():
            db.init_db()

    app.run(debug=True, host="0.0.0.0", port=8090)
