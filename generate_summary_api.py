
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/summary', methods=['POST'])
def generate_summary():
    data = request.json
    name = data.get('startupName')
    revenue = data.get('revenue')
    users = data.get('users')
    growth = data.get('growth')

    if not all([name, revenue, users, growth]):
        return jsonify({"error": "Missing input fields."}), 400

    summary = (
        f"\"{name}\" reports a monthly revenue of ${revenue}, "
        f"with {users} active users and a growth rate of {growth}%. "
        f"This startup shows promising signs of traction and potential scalability."
    )

    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
