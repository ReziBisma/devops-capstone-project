from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = []
next_id = 1

# CREATE
@app.route('/accounts', methods=['POST'])
def create_account():
    global next_id
    data = request.get_json()
    
    account = {
        "id": next_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "address": data.get("address")
    }
    
    accounts.append(account)
    next_id += 1
    
    return jsonify(account), 201

# LIST
@app.route('/accounts', methods=['GET'])
def list_accounts():
    return jsonify(accounts), 200

# READ
@app.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    for acc in accounts:
        if acc["id"] == account_id:
            return jsonify(acc), 200
    return {"error": "Not found"}, 404

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)