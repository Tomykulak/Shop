# app.py (with Flask)
from flask import Flask, render_template, request
from models import init_db
from inventory import list_inventory
from shop import place_order

app = Flask(__name__)
Session = init_db()

@app.route('/')
def home():
    session = Session()
    items = list_inventory(session)
    return render_template('index.html', items=items)

@app.route('/order', methods=['POST'])
def order():
    item_id = request.form['item_id']
    quantity = request.form['quantity']
    session = Session()
    try:
        order = place_order(session, item_id=item_id, quantity=int(quantity))
        return f"Order placed! Total: {order.total_price}"
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
