from flask import Flask
import logging

APP_PORT = 8003

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# ------------------- Dapr pub/sub ------------------- #

# ------------------- Application routes ------------------- #


app.run(port=APP_PORT)