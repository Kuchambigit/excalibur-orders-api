# define what an Order looks like
class Order:
    def __init__(self, order_id, order_date, amount, description):
        # store values in the object
        self.order_id = order_id
        self.order_date = order_date
        self.amount = amount
        self.description = description
