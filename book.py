class Book:



    def __init__(self, book_num):
        self.book_id = book_num

    def __str__(self):
        return str(self.book_id)