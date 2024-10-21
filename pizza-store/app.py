from flask import Flask
from flask_cors import CORS

import logging

DAPR_PORT = 6000

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)

# ------------------- Dapr State Store ------------------- #

# ------------------- Dapr Service Invocation ------------------- #

# ------------------- Dapr Pub/Sub ------------------- #

# ------------------- Application routes ------------------- #

app.run(port=6000)