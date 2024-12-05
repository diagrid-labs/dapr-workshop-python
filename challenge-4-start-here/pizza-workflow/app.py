from flask import Flask, request, jsonify
import logging
import threading

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

APP_PORT = 8005
app = Flask(__name__)

# API endpoints
@app.route('/start-order', methods=['POST'])
def start_order():
    order_data = request.json
    instance_id = f"pizza-order-{order_data['order_id']}"
    
    # TODO: Start the workflow
    
    return jsonify({
        "order_id": order_data["order_id"],
        "workflow_instance_id": instance_id,
        "status": "started"
    })

@app.route('/validate-pizza', methods=['POST'])
def validate_pizza_endpoint():
    validation_data = request.json
    order_id = validation_data["order_id"]
    
    #  TODO: Send the validation data to the workflow
    
    return jsonify({
        "order_id": order_id,
        "validation_status": "approved" if validation_data.get("approved") else "rejected"
    })

@app.route('/get-status/<order_id>', methods=['GET'])
def get_order(order_id):
    instance_id = f"pizza-order-{order_id}"
    
    # TODO: Get the workflow status
    

    return jsonify(result.runtime_status)

@app.route('/pause-order', methods=['POST'])
def pause_order():
    order_data = request.json
    order_id = order_data["order_id"]
    instance_id = f"pizza-order-{order_id}"
    
    # TODO: Pause the workflow
    
    return jsonify({
        "order_id": order_id,
        "status": "paused"
    })

@app.route('/resume-order', methods=['POST'])
def resume_order():
    order_data = request.json
    order_id = order_data["order_id"]
    instance_id = f"pizza-order-{order_id}"
    
    # TODO: Resume the workflow
    
    return jsonify({
        "order_id": order_id,
        "status": "resumed"
    })

@app.route('/cancel-order', methods=['POST'])
def cancel_order():
    order_data = request.json
    order_id = order_data["order_id"]
    instance_id = f"pizza-order-{order_id}"
    
    # TODO: Cancel the workflow
    
    return jsonify({
        "order_id": order_id,
        "status": "cancelled"
    })

if __name__ == "__main__":
    # TODO: Start workflow runtime in a separate thread
    
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=APP_PORT)