
class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.__class__.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book type")
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.__class__.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author type")
        if not isinstance(book, Book):
            raise Exception("Invalid book type")
        if not isinstance(date, str):
            raise Exception("Invalid date type")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties type")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

