"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello from your HTTP server!"})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

greeting_message = "Hello from your HTTP server! How can I assist you today?"

@app.route('/greet', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def greet():
    global greeting_message

    if request.method == 'GET':
        return jsonify({"message": greeting_message})
    
    elif request.method == 'POST':
        data = request.json
        return jsonify({"message": "POST received on /greet", "data": data})
    
    elif request.method == 'PUT':
        data = request.json
        greeting_message = data.get("message", greeting_message)
        return jsonify({"message": "Greeting message replaced", "new_message": greeting_message})
    
    elif request.method == 'PATCH':
        data = request.json
        partial_update = data.get("message")
        if partial_update:
            greeting_message += " " + partial_update
        return jsonify({"message": "Greeting message updated", "new_message": greeting_message})
    
    elif request.method == 'DELETE':
        greeting_message = ""
        return jsonify({"message": "Greeting message deleted"})


@app.route('/echo', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def echo():
    if request.method == 'POST':
        data = request.json
        return jsonify({"you_sent": data})
    
    elif request.method == 'GET':
        return jsonify({"message": "GET received on /echo"})
    
    elif request.method == 'PUT':
        data = request.json
        return jsonify({"message": "PUT received on /echo", "data": data})
    
    elif request.method == 'PATCH':
        data = request.json
        return jsonify({"message": "PATCH received on /echo", "data": data})
    
    elif request.method == 'DELETE':
        return jsonify({"message": "DELETE received on /echo"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
