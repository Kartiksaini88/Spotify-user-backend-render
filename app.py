from flask import Flask, request, jsonify
from flask_cors import CORS
from aws_config import users_table
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)
CORS(app)



@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400


        response = users_table.get_item(Key={"Email": email})
        if 'Item' in response:
            return jsonify({"error": "User already exists"}), 400

        users_table.put_item(
            Item={
                "Email": email,
                "Name": name,
                "Password": password
            }
        )

        return jsonify({"message": "Signup successful!"}), 201

    except ClientError as e:
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Internal server error"}), 500



@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400


        response = users_table.get_item(Key={"Email": email})

        if 'Item' not in response:
            return jsonify({"error": "User not found"}), 404

        user = response['Item']


        if user['Password'] == password:
            return jsonify({"message": "Login successful!", "user": user}), 200
        else:
            return jsonify({"error": "Invalid password"}), 401

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
