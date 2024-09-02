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

class Bookstore:
    def __init__(self):
        self.catalog: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, sale_price: float, purchase_price: float, quantity: int):
        if isbn not in self.catalog:
            new_book = Book(isbn, title,  sale_price, purchase_price, quantity)
            self.catalog[isbn] = new_book

    def delete_book(self, isbn: str):
        if isbn in self.catalog:
            del self.catalog[isbn]

    def search_by_isbn(self, isbn: str)-> Book|None:
        return self.catalog.get(isbn)
    def sell_book(self, isbn: str, copies: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.sell(copies)
    def supply_book(self, isbn: str, copies: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        book.supply(copies)
        return True

    def best_selling_book(self)-> Book|None:
        max_copies_sold = 0
        best_book = None
        if len(self.catalog) <= 0:
            return None
        for book in self.catalog.values():
            copies_sold = book.copies_sold()
            if copies_sold > max_copies_sold:
                max_copies_sold = copies_sold
                best_book = book
        return best_book