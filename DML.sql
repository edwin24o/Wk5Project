
USE LibraryProject;


-- Inserting author info
INSERT INTO authors (id, name, biography) VALUES
(11, 'George R.R. Martin', 'American author, essayist, and critic best known for the A Song of Ice and Fire series.'),
(13, 'Stephen King', 'American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels.'),
(9, 'David Goggins', 'American ultramarathon runner, ultra-distance cyclist, triathlete, and retired Navy SEAL.');

-- Inserting books for George R.R. Martin
INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES
('A Game of Thrones', 11, '101', '1996-08-06', TRUE),
('A Clash of Kings', 11, '102', '1999-11-16', TRUE),
('A Storm of Swords', 11, '103', '2000-10-30', TRUE),
('A Feast for Crows', 11, '104', '2005-10-17', FALSE),
('A Dance with Dragons', 11, '105', '2011-07-12', FALSE);

-- Inserting books for Stephen King
INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES
('The Shining', 13, '106', '1977-01-28', TRUE),
('It', 13, '107', '1986-09-15', FALSE),
('Misery', 13, '108', '1987-06-08', TRUE),
('The Green Mile', 13, '109', '1996-03-01', TRUE);

-- Insertin book for David Goggins
INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES
('Can\'t Hurt Me: Master Your Mind and Defy the Odds', 9, '110', '2018-11-15', TRUE),
('Never Finished: Unshackle Your Mind and Win the War Within', 9, '111', '2022-12-06', TRUE);

-- Inserting users 
INSERT INTO users (id, name, library_id)VALUES 
('33', 'Joe Rogan', 'LR0001'),
('34','Kentaro Miura', 'LR0002'),
('35', 'John Ronald', 'LR0003');


-- Inserting records for borrowed books

-- User 'Joe Rogan' borrowed 'A Feast for Crows'
INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES
((SELECT id FROM users WHERE name = 'Joe Rogan'), 
 (SELECT id FROM books WHERE title = 'A Feast for Crows'), 
 '2024-08-22');

-- User 'Kentaro Miura' borrowed 'A Dance with Dragons'
INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES
((SELECT id FROM users WHERE name = 'Kentaro Miura'), 
 (SELECT id FROM books WHERE title = 'A Dance with Dragons'), 
 '2024-08-22');

-- User 'John Ronald' borrowed 'It'
INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES
((SELECT id FROM users WHERE name = 'John Ronald'), 
 (SELECT id FROM books WHERE title = 'It'), 
 '2024-08-22');