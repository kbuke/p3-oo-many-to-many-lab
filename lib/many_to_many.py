# The Author class should have the following methods:

# contracts(self): This method should return a list of related contracts.
# books(self): method should return a list of related books using the Contract class as an intermediary.
# sign_contract(book, date, royalties): method should create and return new Contract object between author and specified book with specified date and royalties
# total_royalties(): This method should return the total amount of royalties that the author has earned from all of their contracts.

class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return[contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return[contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)   

    def total_royalties(self):
        revenue = sum(contract.royalties for contract in self.contracts())
        return revenue   
    
    

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return[contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return[contract.author for contract in self.contracts()]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("book must be of Book class, date must be a string, and royalties must be an integer")
        else:
            self._author = value
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be of class Book")
        else:
            self._book = value
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        else:
            self._date = value

    @property
    def royalties(self):
        return self._royalties 

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        else:
            self._royalties = value   
    
    @classmethod
    def contracts_by_date(cls, date):
        return[contract for contract in cls.all if date == contract.date]
