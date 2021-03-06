from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'Item1',
                'price': 5.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST -- used to receive data
# GET -- used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string: name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/names'
def get_store(name):
    for store in stores:  # Iterate over stores
        if store['name'] == name:  # If the store name matches, return
            return jsonify(store)  # If no matches, return error message
    return jsonify({'message': 'Store can not be found'})

# GET /store
@app.route('/store')  # convert 'stores' into JSON file
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string: name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_at_store(name):
    request_data = request.get_json()
    for store in stores:  # If store name matches,
        if store['name'] == name:  # Create a new item
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store can not be found'})

# GET /store/<string: name>/item
@app.route('/store/<string:name>/item')  # 'http://127.0.0.1:5000/store/names'
def get_item_at_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store can not be found'})

app.run(port=5000)
