# shop.py
from models import Order, Item

def place_order(session, item_id, quantity):
    item = session.query(Item).get(item_id)
    if item and item.stock >= quantity:
        total_price = item.price * quantity
        order = Order(item_id=item_id, quantity=quantity, total_price=total_price)
        session.add(order)
        item.stock -= quantity  # Decrease stock
        session.commit()
        return order
    else:
        raise ValueError("Item out of stock or invalid quantity")
