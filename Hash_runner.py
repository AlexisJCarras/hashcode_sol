from library import Library
from book import Book


libraries = []
num_of_books = 0
num_of_libs = 0
max_scan_days = 0
book_scores = []


counter = 0
current_library = None

with open('a_example.txt') as input:
    for line in input:
        
        line = line.strip('\n')

        line_array = line.split(" ")
    
        # first line
        if (counter == 0):
            num_of_books = int(line_array[0])
            num_of_libs = int(line_array[1])
            max_scan_days = int(line_array[2])
        
        # second line
        elif(counter==1):
            book_scores = list(map(int, line_array))

        # desc of lib
        elif(counter != 0 and counter != 1 and counter % 2 == 0):
            current_library = Library(line_array[0], line_array[1], line_array[2])

        # contents of lib
        elif(counter != 0 and counter != 1 and counter % 2 == 1):
            for book in line_array:
                current_library.add_book(Book(book))

            libraries.append(current_library)
        

        counter = counter + 1



# print(num_of_books)
# print(num_of_libs)
# print(max_scan_days)
# print(book_scores)

for l in libraries:
    print(l)
    for book in l.books:
        print(book)







