import random
import sys
#menu:
    # add book
        #enter book name
        #create instance of book
        #add it to read or unread

    # view books
        #view books in read or unread list
            # select book
                #delete book 
                # mark as read or unread, depending on where the book is

# randomly choose pick from unread "list" to read

# def replace_line(file,old_line,new_line):
#             f = open(file,'r')
#             data = f.read()
#             f.close()

#             new_data = data.replace(old_line,new_line)

#             f = open(file,'w')
#             f.write(new_data)
#             f.close

#         old_password = input('Enter current password: ')
#         while old_password!=self.password:
#             print('The password you entered is incorrect.\n')

#             old_password = input('Please try again: ')

UNREAD_FILE = "unread_books.txt"
READ_FILE = "read_books.txt"

class Book:

    def __init__(self,title):
        self.title = title

    @classmethod
    def view_read(cls):
        with open(READ_FILE,'r') as f:
            for line in f:
                print(line)

    @classmethod
    def view_unread(cls):
        with open(UNREAD_FILE,'r') as f:
            for line in f:
                print(line)
    
    @classmethod
    def select_book(cls,book_title,book_file):
        with open(book_file,'r') as f:
            for line in f:
                if book_title.lower()+'\n' == line.lower():
                    return Book(book_title)
                else:
                    pass
            return False
    

    def remove_book(self,file_name):
        with open(file_name,'r') as f:
            lines = f.readlines()
        
        with open(file_name,'w') as f:
            for line in lines:
                if line != self.title+'\n':
                    f.write(line)
        





    def add_to_unread(self):
        with open(UNREAD_FILE,'a') as f:
            f.write(self.title+'\n')
            print(f'{self.title} added to unread books')

    def add_to_read(self):
        with open(READ_FILE,'a') as f:
            f.write(self.title+'\n')
            print(f'{self.title} added to read books')

def add_books():
    book_title = input('Enter title of book or 3 to go back: ')
    if book_title == '3':
        start()
    else:
        book = Book(book_title)


    print('=======ADD BOOKS=======\n')
    print('1. Add book to read list\n2. Add book to unread list\n3. Go back \n')
    choice = input('Enter choice: ')

    while choice!= '1' and choice!= '2' and choice!= '3':
        print('Invalid input. Try again.\n')
        choice = input('Enter choice: ')

    
    #Add to read list
    if choice == '1':
        book.add_to_read()

        choice = input('Enter 1 to add another book or 2 to go back: ')
        while choice!='1' and choice!='2':
            print('Invalid input\n')
            choice = input('Enter 1 to add another book or 2 to go back: ')
        
        if choice == '1':
            add_books()
        elif choice == '2':
            start()

    #Add to unread list    
    elif choice == '2':
        book.add_to_unread()
        
        choice = input('Enter 1 to add another book or 2 to go back: ')
        while choice!='1' and choice!='2':
            print('Invalid input\n')
            choice = input('Enter 1 to add another book or 2 to go back: ')
        
        if choice == '1':
            add_books()
        elif choice == '2':
            start()

    #Back to start
    elif choice == '3':
        start()

def view_books():
    print('=======VIEW BOOKS=======\n')
    print('1. View unread books\n2. View read books\n3. Go back\n')
    choice = input('Enter choice: ')

    while choice!= '1' and choice!= '2' and choice!= '3':
        print('Invalid input. Try again.\n')
        choice = input('Enter choice: ')

    #view unread
    if choice == '1':
        Book.view_unread()

        book_selection = input('Enter title of book to select, or 3 to go back: ')
        if book_selection == '3':
            view_books()
        else:
            book = Book.select_book(book_selection,UNREAD_FILE)
            while book == False:
                print('The title you entered is not in this list.\n')
                book_selection = input('Enter title of book to select it, or 3 to go back: ')
                if book_selection == '3':
                    view_books()
                else:
                    book = Book.select_book(book_selection,UNREAD_FILE)
    
            print(f'"{book.title}" selected.\n') 

            print(f'1. Mark book as read\n2. Delete\n3. Go back \n') #<----
            choice = input('Enter choice: ')

            while choice!= '1' and choice!= '2' and choice!= '3':
                print('Invalid input. Try again.\n')
                choice = input('Enter choice: ')
            
            if choice =='1':
                book.remove_book(UNREAD_FILE)
                book.add_to_read()
                #add line to go back
            

    #view read
    elif choice == '2':
        Book.view_read()

        book_selection = input('Enter title of book to select, or 3 to go back: ')
        if book_selection == '3':
            view_books()
        else:
            book = Book.select_book(book_selection,READ_FILE)
            while book == False:
                print('The title you entered is not in this list.\n')
                book_selection = input('Enter title of book to select it, or 3 to go back: ')
                if book_selection == '3':
                    view_books()
                else:
                    book = Book.select_book(book_selection,READ_FILE)
    
            print(f'"{book.title}" selected.')
            print(f'1. Mark book as unread\n2. Delete\n3. Go back \n') 
            choice = input('Enter choice: ')

            while choice!= '1' and choice!= '2' and choice!= '3':
                print('Invalid input. Try again.\n')
                choice = input('Enter choice: ')
            
            if choice =='1':
                book.remove_book(READ_FILE)
                book.add_to_unread()

    #go back to start
    elif choice == '3':
        start()
    












def start():
    print('======BOOK ORGANIZER======\n')
    print('1. Add a book\n2. View books\n3. Get a new book to read\n4. Exit\n')
    choice = input('Enter choice: ')

    while choice!= '1' and choice!= '2' and choice!= '3' and choice!= '4':
        print('Invalid input. Try again.\n')
        choice = input('Enter choice: ')
    
    #Add book
    if choice == '1':
        add_books()
    

    if choice == '4':
        print('Exiting program...')
        sys.exit()
        
        
    
    # View books
    if choice == '2':
        view_books()



start()
