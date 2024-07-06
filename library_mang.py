
# Library Management In Python 

class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book) 
        self.noOfBooks = len(self.books)
        
    def showInfo(self):
        print(f"Now you have {self.noOfBooks} books in library.")

l1 = Library()
l1.addBook("Stranger Things.")
l1.addBook("Harry Potter.")
l1.addBook("Money Heist.")
l1.showInfo()