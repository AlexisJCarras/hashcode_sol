from library import Library
from book import Book




def file_reader(file):
    
    libraries = []
    with open(file) as input:
        for line in input:
            libraries.append(line)
    return libraries 



# library0 = Library(0,4,2)
# library2 = Library(2,4,2)
# book0 = Book(0,5)

# library0.add_book(book0)

# print(library0.books)

libraries = file_reader("a_example.txt")
print(libraries[2])










