from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

# Endpoint #1: /


@hello_world_bp.get("/")
def endpoint_name():
    response_massage = "Hello, World!"
    return response_massage


# 127.0.0.1 - - [15/Apr/2025 20:34:34] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [15/Apr/2025 20:34:44] "GET / HTTP/1.1" 200 -
# * Running on http://127.0.0.1:5000
# Press CTRL+C to quit


# ada
@hello_world_bp.get("/")
def say_hello_world():
    return "Hello, World!"


# Endpoint #2: /hello/JSON
@hello_world_bp.get("/hello/JSON")
def say_hello_json():
    return {
        "name": "Ada Tatyana",
        "message": "Hello!",
        "hobbies": ["Hiking", "Sleeping", "Watching Reality Shows"],
    }


# Endpoint #3: Debugging a Broken Endpoint
@hello_world_bp.get("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body
