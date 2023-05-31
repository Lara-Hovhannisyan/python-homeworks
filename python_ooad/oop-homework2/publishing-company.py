class Publication:
    def __init__(self, title:str, price:int):
        self.title = title
        self.price = price

    def setData(self):
        self.title = input("Enter publication title: ")
        self.price = int(input("Enter publication price: "))

    def getData(self):
        print("Publication Title:", self.title)
        print("Publication Price:", self.price)

class Book(Publication):
    def __init__(self, title, price, count_of_pages):
        super().__init__(title, price)
        self.count_of_pages = count_of_pages

    def setData(self):
        super().setData()
        self.count_of_pages = int(input("Enter count of pages: "))

    def getData(self):
        super().getData()
        print("Count of Pages:", self.count_of_pages)

class Tape(Publication):
    def __init__(self, title, price, playing_time):
        super().__init__(title, price)
        self.playing_time = playing_time

    def setData(self):
        super().setData()
        self.playing_time = int(input("Enter playing time (in minutes): "))

    def getData(self):
        super().getData()
        print("Playing Time (minutes):", self.playing_time)



if __name__ == "__main__":
    book = Book("", 0, 0)
    tape = Tape("", 0, 0)

    print("--- Book ---")
    book.setData()
    print("\n--- Tape ---")
    tape.setData()

    print("\n--- Book Details ---")
    book.getData()
    print("\n--- Tape Details ---")
    tape.getData()