class Books:
    Book_Type = ("Hardcover", "Paperback", "E-Book")
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
    def setnewprice(self, newprice):
        self.newprice = newprice
    def getprice(self):
        return self.price
    def getnewprice(self):
        return self.newprice
    def updateprice(self):
        self.price = self.newprice

Book1 = Books("The God Delusion", "Richard Dawkins", 399)
Book2 = Books("The Blind Watchmaker", "Richard Dawkins", 499)
Book3 = Books("Dragons Of Eden", "Carl Sagan", 260)
Book4 = Books("The Vital Question", "Nick Lane", 350)
Book5 = Books("The Theory of Everything", "Stephen Hawkings", 250)
Book6 = Books("Bhagwad Gita", "Vyasa", 100)
Book7 = Books("12 Rules For Life", "Jordan Peterson", 500)
Book8 = Books("The Story Of Your Life and Others", "Ted Chiang", 290)

print(Book4.name)
print(Book6.author)
print(Book7.name, " ", Book7.author, " ", Book7.price)
print(Book2.getprice())

Book1.setnewprice(699)
Book1.updateprice()
print("The new price for The God Delusion is:", Book1.getnewprice())
print(Book1.name, " ", Book1.author, " ", Book1.price)

print(type(Book8))
print(Books.Book_Type)
