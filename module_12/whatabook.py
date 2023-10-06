import sys
import mysql.connector
from mysql.connector import Error

#\start of the connection for the functions 
my_db= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='cybr41018!',
    db='whatabook')

_cursor=my_db.cursor()

#\ All functions start here
#\ show_menu()- display menu and ask which menu to go next

def show_menu():
    print("\n Welcome to our menu")
    print(" \n 1. Store Locations \n 2. View Books \n 3. My account"
    )

    try:
        user_input= int(input('Enter number of the menu: '))

        return user_input
    except ValueError:
        print("Invalid input")
        
        sys.exit(0)

#\show_books is supposed to display all 9 books 
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author ,details FROM book;")
    book_result= _cursor.fetchall()

    for book in book_result:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))
        
#\show_location display the location address
def show_locations(_cursor):
    _cursor.execute("Select store_id,locale from store;")
    store_result=_cursor.fetchall()
    for store in store_result:
        print('Store Location:{}'.format(store[1]))
        
        sys.exit(0)
    
#\validate_user is supposed to validate the user's identity since the are only three user id 1-3
def validate_user(): 
    try:
        user_input_id= int(input('Please provide us with your user ID: '))

        if user_input_id <= 0 or user_input_id > 3:
            print('Invalid ID')
            sys.exit(0)
        return user_input_id
    except ValueError: 
        print('That is an invalid input.')
        
        sys.exit(0)

#\ show_account_menu() once a user's id is validated
#\it will display their Wishlist
#\Add book or return to main menu
def show_account_menu():
    try:
        print('\nAccount Menu \n1. Wishlist \n2. Add Book \n3. Main Menu ')
        user_input_account= int(input('Enter number of menu:  '))
        return user_input_account
    
    except ValueError:
        print("That is invalid number")
        
        sys.exit(0)
    
#\ Was not able to get this function to work correctly 
#\ had to copy and paste it from github repository
#\ show user's wishlist but was infinite 
def show_wishlist(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n Wishlist Item")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

#\ show books not in a user's wishlist
def show_books_to_add(_cursor, _user_id):
    """ query the database for a list of books not in the users wishlist """

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n Available Books")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1], book[2], book[3]))
#\add_book_to_wishlist is supposed to add to a user's wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


#\ The start of the program

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='cybr41018!',
    db='whatabook') # connect to the WhatABook database 

cursor = db.cursor() # cursor for MySQL queries

print("\n  Welcome to the WhatABook Application! ")

user_input= show_menu()

while user_input !=4:
    if user_input == 1:
        show_locations(cursor)
#\When the show_books(cursor) runs it goes in an infinite loop.... 
    if user_input == 2:
        show_books(cursor)

    if user_input == 3:
        input_user_id= validate_user()
        account_option= show_account_menu()

        while input_user_id !=3:

            if input_user_id == 1: 
                show_wishlist(cursor,input_user_id)
#/ show_wishlist ask to add a book when it should just show the what is in the wishlist 
            
            if input_user_id == 2: 
                show_books_to_add(cursor,input_user_id)
                book_id= int(input('\n Enter the ID of the book you want to add: '))
                add_book_to_wishlist(cursor,input_user_id,book_id)

                db.commit()

                print('\n Book ID: {} was added to your wishlist'.format(book_id))
            if input_user_id < 0 or input_user_id >3:
                print ('\n Invalid input, try again')
            

        print('Program terminated')         