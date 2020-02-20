from library import Library
from book import Book
import sys

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





# libraries
# num_of_books
# num_of_libs
# max_scan_days 
# book_scores


comp_signuptime = sys.maxsize
lib = None
days_needed = 0
num_of_lib_to_scan = 0

for library in libraries:

    if (int(library.signup_time) < int(comp_signuptime)):
        comp_signuptime = library.signup_time
        lib = library


days_needed = days_needed + lib.signup_time
    




print(lib)