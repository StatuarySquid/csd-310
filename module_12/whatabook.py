import sys
import mysql.connector
from mysql.connector import Error

my_db= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='cybr41018!',
    db='whatabook')

cursor=my_db.cursor()

'''cursor.execute("SELECT book_id, book_name, details_v,author FROM book;")

book_result= cursor.fetchall()

for book in book_result:
    print('The book id: {}'.format(book[0]))
    print('The book name: {}'.format(book[1]))
    print('The book detail: {}'.format(book[2]))
    print('The author: {}'.format(book[3]))
    print('')'''

def show_menu():
    print("\n Welcome to our menu")
    print(" \n 1. Store Locations \n 2. View Books \n 3. My account"
    )

    try:
        user_input= int(input('Enter number of menu \n1-Store \n2-Books\n3-Account \n4-Exit \n '))

        return user_input
    except ValueError:
        print("Invalid input")

        sys.exit(0)

def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author,details_v FROM book;")
    book_result= cursor.fetchall()

    for book in book_result:
        print('Book name: {}'.format(book[1]))
        print('Author: {}'.format(book[2]))
        print('Description: {}'.format(book[3]))
        print('')

def show_locations(cursor):
    cursor.execute("Select store_id,locale from store;")
    store_result=cursor.fetchall()
    for store in store_result:
        print('Store Location:{}'.format(store[1]))

def validate_user(): 

    while True:
        try:
            user_input_id= int(input('Please provide us with your user ID: '))

            if user_input_id <= 0 or user_input_id > 3:
                print('Invalid ID')
                sys.exit(0)
            return user_input_id
        except ValueError: 
            print('That is an invalid input.')
            continue

def show_account_menu():
    
    while True:
        try:
            print('\nAccount Menu \n1. Wishlist \n2. Add Book \n3. Main Menu ')
            user_input_account= int(input('Enter number of menu:  '))
            return user_input_account
        except ValueError:
            print("That is invalid number")
            continue
    
def show_wishlist(cursor,user_id)
    cursor.
