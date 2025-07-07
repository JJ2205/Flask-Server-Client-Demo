"""
import requests

# Send GET
resp = requests.get("http://127.0.0.1:5000/greet")
print("GET Response:", resp.json())

# Send POST
payload = {"sensor": "temperature", "value": 28}
resp = requests.post("http://127.0.0.1:5000/echo", json=payload)
print("POST Response:", resp.json())
"""

import requests

BASE_URL = "http://127.0.0.1:5000"

# ---------- /greet endpoint ----------

# GET /greet
resp = requests.get(f"{BASE_URL}/greet")
print("GET /greet:", resp.json())

# POST /greet
payload_post = {"user": "Jobin", "action": "testing POST"}
resp = requests.post(f"{BASE_URL}/greet", json=payload_post)
print("POST /greet:", resp.json())

# PUT /greet (replace greeting message)
payload_put = {"message": "Hello Jobin, welcome back!"}
resp = requests.put(f"{BASE_URL}/greet", json=payload_put)
print("PUT /greet:", resp.json())

# PATCH /greet (append to message)
payload_patch = {"message": "How can I help you today?"}
resp = requests.patch(f"{BASE_URL}/greet", json=payload_patch)
print("PATCH /greet:", resp.json())

# DELETE /greet (clear the message)
resp = requests.delete(f"{BASE_URL}/greet")
print("DELETE /greet:", resp.json())

# ---------- /echo endpoint ----------

# GET /echo
resp = requests.get(f"{BASE_URL}/echo")
print("GET /echo:", resp.json())

# POST /echo
payload_post = {"sensor": "temperature", "value": 28}
resp = requests.post(f"{BASE_URL}/echo", json=payload_post)
print("POST /echo:", resp.json())

# PUT /echo
payload_put = {"update": "This is a full update"}
resp = requests.put(f"{BASE_URL}/echo", json=payload_put)
print("PUT /echo:", resp.json())

# PATCH /echo
payload_patch = {"note": "Just a partial update"}
resp = requests.patch(f"{BASE_URL}/echo", json=payload_patch)
print("PATCH /echo:", resp.json())

# DELETE /echo
resp = requests.delete(f"{BASE_URL}/echo")
print("DELETE /echo:", resp.json())
