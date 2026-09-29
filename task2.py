import sqlite3

# Connect to database (creates library.db file)
conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Create books table and populate with 8 records
cur.executescript("""
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price REAL,
    stock INTEGER
);

INSERT INTO books VALUES
(1, 'Data Science Basics', 'Tech', 1450, 10),
(2, 'Clean Code', 'Tech', 1200, 8),
(3, 'The Silent Patient', 'Fiction', 1350, 2),
(4, 'Python Crash Course', 'Tech', 950, 15),
(5, 'Atomic Habits', 'Self-Help', 1100, 12),
(6, 'To Kill a Mockingbird', 'Fiction', 800, 3),
(7, '1984', 'Fiction', 900, 4),
(8, 'The Hobbit', 'Fiction', 1050, 1);
""")
conn.commit()

# Query (a) & (b): Select title as book_title, price > 1000, sorted descending
print("Books above Rs.1000 (sorted):")
cur.execute("""
SELECT title AS book_title, price 
FROM books 
WHERE price > 1000 
ORDER BY price DESC;
""")
for row in cur.fetchall():
    print(row)

print("\nLow-stock Fiction books:")
# Query (c): Select Fiction books with stock < 5
cur.execute("""
SELECT title, genre, price, stock 
FROM books 
WHERE genre = 'Fiction' AND stock < 5;
""")
for row in cur.fetchall():
    print(row)

conn.close()