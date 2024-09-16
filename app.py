from flask import Flask, render_template, request, redirect, url_for
from database import init_db
from inventory import list_inventory, list_orders
from shop import place_order

app = Flask(__name__)
Session = init_db()

@app.route('/')
def home():
    session = Session()
    items = list_inventory(session)
    orders = list_orders(session)
    return render_template('index.html', items=items, orders=orders)

# Route to handle order submissions
@app.route('/order', methods=['POST'])
def order():
    session = Session()
    item_id = int(request.form['item_id'])
    quantity = int(request.form['quantity'])

    # Try to place the order
    try:
        order = place_order(session, item_id=item_id, quantity=quantity)
        return redirect(url_for('home'))  # Redirect back to the home page after placing the order
    except ValueError as e:
        return str(e), 400  # Show error message if stock is insufficient

if __name__ == '__main__':
    app.run(debug=True)
