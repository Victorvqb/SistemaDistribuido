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
    return jsonify({"message": "Data created successfully"})

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
    return jsonify({"message": "Data updated successfully"})

# Delete 
@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    db.child("users").child(data["id"]).remove()
    return jsonify({"message": "Data deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)