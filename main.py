from flask import Flask, request, jsonify
import pyrebase

app = Flask(__name__)

# Init Firebase
config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Create 
@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    db.child("users").push(data)
    return jsonify({"message": "Criado com sucesso"})

# Read 
@app.route('/read', methods=['GET'])
def read():
    users = db.child("users").get()
    return jsonify({"users": users.val()})

# Update 
@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    db.child("users").child(data["id"]).update(data)
    return jsonify({"message": "Atualizado com sucesso"})

# Delete 
@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    db.child("users").child(data["id"]).remove()
    return jsonify({"message": "Deletado com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)