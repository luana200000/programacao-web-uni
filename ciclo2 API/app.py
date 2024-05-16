"""
Engenharia de Software - UniEVANGÉLICA
Programação Web
Dev: Luana Teixeira de Moraes
12/05/2024
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [
    {
        'id': 1,
        'modelo': 'SW4',
        'marca': 'Toyota'
    },
    {
        'id': 2,
        'modelo': 'Hilux',
        'marca': 'Toyota'
    },
    {
        'id': 3,
        'modelo': 'Argo',
        'marca': 'Fiat'
    }
]

#GET /api/cars - recuperar a lista de carros

@app.route('/cars', methods=['GET'])
def get_car():
    return jsonify(cars)

#POST /api/cars - criar um novo carro

@app.route('/cars', methods=['POST'])
def post_new_car():
    new_car = request.get_json()
    cars.append(new_car)
    return jsonify(cars)

#GET /api/cars/{car_id} - recuperar informações de um carro específico por ID

@app.route('/cars/<int:id>', methods=['GET'])
def get_car_by_id(id):
    for car in cars:
        if car.get('id') == id:
            return jsonify(car)

#PUT /api/cars/{car_id} - atualizar informações de um carro específico por ID

@app.route('/cars/<int:id>', methods=['PUT'])
def edit_car_by_id(id):
    edited_car = request.get_json()
    for index, car in enumerate(cars):
        if car.get('id') == id:
            cars[index].update(edited_car)
            return jsonify(cars[index])

#DELETE /api/cars/{car_id} - excluir um carro específico por ID

@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    for index, car in enumerate(cars):
        if car.get('id') == id:
            del cars[index]
    
    return jsonify(cars)


app.run(port=5000, host='localhost', debug=True)