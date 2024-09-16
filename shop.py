# shop.py
from models import Order, Item


def place_order(session, item_id, quantity):
    item = session.query(Item).get(item_id)

    # Check if the item exists and has enough stock
    if item is None:
        raise ValueError("Item not found.")
    if item.stock < quantity:
        raise ValueError("Not enough stock to fulfill the order.")

    # Deduct stock and create an order
    item.stock -= quantity
    total_price = item.price * quantity

    order = Order(item_id=item_id, quantity=quantity, total_price=total_price)
    session.add(order)

    # Commit the changes to the database
    session.commit()

    return order
