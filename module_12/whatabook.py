import mysql.connector
from mysql.connector import Error

my_db= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='cybr41018!',
    db='whatabook')

cursor=my_db.cursor()

cursor.execute("SELECT book_id, book_name, details_v,author FROM book;")

book_result= cursor.fetchall()

for book in book_result:
    print('The book id: {}'.format(book[0]))
    print('The book name: {}'.format(book[1]))
    print('The book detail: {}'.format(book[2]))
    print('The author: {}'.format(book[3]))
    print('')