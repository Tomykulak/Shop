from models import Item

def add_item(session, name, price, stock):
    item = Item(name=name, price=price, stock=stock)
    session.add(item)
    session.commit()

def get_item_by_name(session, name):
    return session.query(Item).filter(Item.name == name).first()

def update_item_stock(session, item_id, quantity):
    item = session.query(Item).get(item_id)
    if item:
        item.stock += quantity
        session.commit()

def list_inventory(session):
    return session.query(Item).all()