from create_sale import batch_iterator
from models import Purchase
from utils import engine, session

batches = session.query(Purchase.id, Purchase.in_stock).filter(
    Purchase.product_id == 7).order_by(Purchase.created_at.asc()).all()

print(batches)

print(batch_iterator(5000, batches=batches))
