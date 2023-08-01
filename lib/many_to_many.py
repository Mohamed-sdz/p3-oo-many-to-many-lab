class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise TypeError("book must be of type Book")
        if not isinstance(date, str):
            raise TypeError("date must be of type str")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be of type int")

        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.__class__.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set([contract.author for contract in self.contracts()]))

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be of type Author")
        if not isinstance(book, Book):
            raise TypeError("book must be of type Book")
        if not isinstance(date, str):
            raise TypeError("date must be of type str")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be of type int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda x: x.date)