from flask import Flask, request
import socket

app = Flask(__name__)


@app.route('/', methods=['POST'])
def receive_data():
    json = request.json
    print(json)
    return json, 200


if __name__ == '__main__':
    app.run(debug=True)
    # Get the active port
    port = socket.socket().getsockname()[1]
    print("Active port:", port)
