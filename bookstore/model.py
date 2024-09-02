from datetime import datetime


# TODO: Add code here
class Transaction:
    SELL: int = 1
    SUPPLY: int = 2
    def __init__(self, type: int, copies: int):
        self.type = type
        self.copies = copies
        self.date:datetime = datetime.now()

class Book:
    def __init__(self, isbn: str, title: str, sale_price: float, purchase_price: float, quantity: int):
        self.isbn: str = isbn
        self.title: str = title
        self.sale_price: float = sale_price
        self.purchase_price: float = purchase_price
        self.quantity: int = quantity
        self.transactions: list[Transaction] = []

    def sell(self, copies: int) -> bool:
        if copies >= self.quantity:
            return False
        else:
            self.quantity -= copies
            self.transactions.append(Transaction(Transaction.SELL, copies))
            return True

    def supply(self, copies: int):
        self.quantity += copies
        self.transactions.append(Transaction(Transaction.SUPPLY, copies))

    def copies_sold(self)-> int:
        total_sold = sum(transaction.copies for transaction in self.transactions if transaction.type == Transaction.SELL)
        return total_sold

    def __str__(self) -> str:
        return f"ISBN: {self.isbn}\nTitle: {self.title}\nSale Price: {self.sale_price}\nPurchase Price: {self.purchase_price}\nQuantity: {self.quantity}"