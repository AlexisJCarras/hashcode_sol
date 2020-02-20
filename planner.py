from library import Library 

def Planner(self, array, deadline):# array_of_libaries_sorted (array) in ascending order of sign up times


       

    i = -1
    scanning = 0
    days_needed = 0

    while (deadline >= days_needed):    

        i += 1
        choice = arr[i] #should be the library with the smallest signup time

        days_needed  = arr[i].signuptime

        for b in range(number_of_books):
            
            if((number_of_books % max_books_perday) == 0):
                days_needed += 1
                scanning += 1

        for l in range(len(array)):
            if (((array[i].signup_time) - scanning) < selected):
                selected = array[i] 

