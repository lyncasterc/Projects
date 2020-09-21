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
    
    @classmethod
    def get_random_book(cls):
        with open(UNREAD_FILE,'r') as f:
            lines = f.readlines()
        random.shuffle(lines)
        random_book = random.choice(lines)
        return random_book


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
            #move to read
            if choice =='1':
                book.remove_book(UNREAD_FILE)
                book.add_to_read()
                print(f'"{book.title}" moved to read books list. ')
                view_books()

            #delete
            elif choice == '2':
                book.remove_book(UNREAD_FILE)
                print(f'"{book.title}" deleted.')
                view_books()
            

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
            #move to unread
            if choice =='1':
                book.remove_book(READ_FILE)
                book.add_to_unread()
                print(f'"{book.title}" moved to unread books list. ')
                view_books()

            #delete
            elif choice == '2':
                book.remove_book(READ_FILE)
                print(f'"{book.title}" deleted.')
                view_books()

    #go back to start
    elif choice == '3':
        start()

def random_book():
    choice = input('Enter 1 to recieve a random book suggestion or 2 to go back: ')
    while choice != '1' and choice != '2':
        print('Invalid input.\n')
        choice = input('Enter 1 to recieve a random book suggestion or 2 to go back: ')
    if choice == '1':
        random_book = Book.get_random_book()
        print(f'Your random book suggestion is {random_book}!')
        start()
    if choice == '2':
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

    # View books
    elif choice == '2':
        view_books()

    # random book suggestion
    elif choice =='3':
        random_book()

    #quit program
    elif choice == '4':
        print('Exiting program...')
        sys.exit()



start()
