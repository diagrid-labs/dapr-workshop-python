from flask import Flask, request, jsonify
import json
import logging

APP_PORT = 8001

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/orders-sub', methods=['POST'])
def orders_subscription():
    """Handle order updates from pub/sub"""
    event = request.json
    
    try:
        # Get the order data from the event
        order_data = json.loads(event['data'])
        order_id = order_data['order_id']
        
        logger.info(f"Received order update for order {order_id}: {order_data['status']}")
        
        # TODO: Update the order state
        
        return jsonify({'success': True})
        
    except Exception as e:
        logger.error(f"Error processing order update: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/order', methods=['POST'])
def create_order():
    """Create a new order"""
    order_data = request.json
    order_id = order_data['order_id']
    
    try:
        logger.info("Save order")

        # TODO: Save the order data to the state store
        
        return jsonify({'success': True})
        
    except Exception as e:
        logger.error(f"Error creating order {order_id}: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    """Get order details from state store"""
    try:
        logger.info("Get order")

        # TODO: Get the order data from the state store
            
    except Exception as e:
        logger.error(f"Error getting order {order_id}: {str(e)}")
        return jsonify({'error': str(e)}), 500
    
@app.route('/order/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete order details from state store"""
    try:
        logger.info("Delete order")

        # TODO: Delete the order data from the state store
            
    except Exception as e:
        logger.error(f"Error deleting order {order_id}: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(port=APP_PORT)