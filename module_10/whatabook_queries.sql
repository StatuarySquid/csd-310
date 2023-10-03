-- Active: 1696128538988@@localhost@3306@whatabook

/*
    Wishlist items 
*/
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

/*
    Store location 
*/
SELECT store_id, locale from store;

/*
    Full listing of the books WhatABook offers
*/
SELECT book_id, book_name, author, details_v from book;

/*
    User wishlist
*/
SELECT book_id, book_name, author, details_v
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);

/*
    Insert book into wishlist. AUTO INCREMENT BUT IT IS STILL ASKING FOR DEFAULT VALUE
*/
INSERT INTO wishlist(wishlist_id, user_id, book_id)
    VALUES(5, 1, 9)

/*
    Removing book
*/
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;