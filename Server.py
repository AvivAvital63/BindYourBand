from flask import Flask
from flask import jsonify
import os
from datetime import datetime


app = Flask(__name__)
messages = []


@app.route('/', methods=['GET'])
def return_all():
    return jsonify({'messages': messages})


@app.route('/', methods=['POST'])
def addOne():
    message = "Client Sent To Server At: " + str(datetime.now())
    messages.append(message)
    return jsonify({'messages': messages})


def main():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7777)))


if __name__ == "__main__":
    main()
