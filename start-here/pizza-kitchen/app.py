from flask import Flask, request, jsonify
import json
import time
import logging

APP_PORT = 8003

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def cook_pizza(order_data):
    """Cook the pizza and update its status through the process"""
    try:
        # Simulate cooking stages
        stages = [
            ('preparing_ingredients', 2),
            ('making_dough', 3),
            ('adding_toppings', 2),
            ('baking', 5),
            ('quality_check', 1)
        ]
        
        # TODO: Update the order status for each stage
        
        order_data['status'] = 'cooked'
        logger.info(f"Order {order_data['order_id']} - cooking completed")
        
        return order_data
        
    except Exception as e:
        logger.error(f"Error cooking pizza: {str(e)}")
        order_data['status'] = 'cooking_failed'
        order_data['error'] = str(e)
        return order_data

@app.route('/cook', methods=['POST'])
def start_cooking():
    """Handle cooking requests"""
    order_data = request.json
    logger.info(f"Starting cooking for order: {order_data['order_id']}")
    
    # Cook the pizza
    result = cook_pizza(order_data)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=APP_PORT)