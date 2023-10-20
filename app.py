from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Inicializando base de datos de pedidos (en realidad, una lista)
orders = []

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = {
        'id': orders[-1]['id'] + 1 if orders else 1,
        'customer_name': data['customer_name'],
        'total_price': data['total_price'],
        'order_date': datetime.utcnow().isoformat(),
        'products': data['products']
    }
    orders.append(new_order)
    return jsonify(new_order), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(debug=True)