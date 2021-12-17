"""Creates sale and links it to a batch utilizing FIFO exit method."""

from models import Sale, SaleToPurchase, Purchase

from utils import session
import sys
#args = [10, '2021-06-09 10:32:46', 25, 6]

arguments = sys.argv


def batch_iterator(quantity: int, batches: list[tuple[int]]) -> None:

    batches = [list(i) for i in batches]

    used_stock = []

    for row in batches:

        original_stock = row[-1]
        row[-1] -= quantity

        if row[-1] < 0:

            quantity -= original_stock
            row[-1] = 0
            used_stock.append((row[0], original_stock))

        else:
            used_stock.append((row[0], quantity))
            break

    return [tuple(i) for i in batches], used_stock


def sale_creator(arguments: list[int, str]) -> None:
    """Registers a sale in the destination database."""

    product_id = int(arguments[1])
    created_at = arguments[2]
    quantity = int(arguments[3])
    customer_id = int(arguments[4])

    batches = session.query(Purchase.id, Purchase.in_stock).filter(
        Purchase.product_id == product_id).order_by(Purchase.created_at.asc()).all()
    # Batches are returned in ascending order (filtered by created_at) for FIFO exit method.

    new_batches, used_stock = batch_iterator(
        quantity=quantity, batches=batches)

    """Gets batches necessary to fulfill the quantity required by the sale and modifies stock in those rows."""
    for i in range(len(batches)):
        if batches[i] != new_batches[i]:

            session.query(Purchase).filter(
                Purchase.id == new_batches[i][0]
            ).update({"in_stock": f"{new_batches[i][1]}"})

            session.commit()
        else:
            break

    """Creates and commits the sale table row."""
    new_sale = Sale(product_id=product_id, created_at=created_at,
                    quantity=quantity,  customer_id=customer_id)

    session.add(new_sale)
    session.commit()

    """Creates and commits all purchases linked to the sale to the sale_to_purchase table."""
    new_sale_id = session.query(Sale.id).order_by(
        Sale.created_at.desc()).first()

    for purchase_id, stock_used in used_stock:
        new_sale_to_purchase = SaleToPurchase(
            sale_id=new_sale_id[0], purchase_id=purchase_id, quantity=stock_used)

        session.add(new_sale_to_purchase)
        session.commit()

    print('New sale added successfully.')
    print('Corresponding tables where modified as expected.')


if __name__ == '__main__':

    sale_creator(arguments=arguments)
