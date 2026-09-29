import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# Database Setup
cur.executescript("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1, 'Ali', 'Islamabad'),
(2, 'Sara', 'Lahore'),
(3, 'Bilal', 'Islamabad'),
(4, 'Usman', 'Karachi'),
(5, 'Zainab', 'Lahore'),
(6, 'Ayesha', 'Rawalpindi');

INSERT INTO orders VALUES
(1, 1, 4500), (2, 1, 7200),
(3, 2, 3000), (4, 3, 9800),
(5, 4, 2500), (6, 4, 1500),
(7, 5, 8600), (8, 5, 3000),
(9, 6, 4000), (10, 6, 2000);
""")
conn.commit()

# Query (a): INNER JOIN customers and orders
print("Customer orders (joined):")
cur.execute("""
SELECT c.name, o.amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
""")
for row in cur.fetchall():
    print(row)

# Query (b): Total spend per customer
print("\nTotal spend per customer:")
cur.execute("""
SELECT c.name, SUM(o.amount) AS total_spend
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spend DESC;
""")
for row in cur.fetchall():
    print(row)

# Query (c): Cities with average order amount > 5000
print("\nCities with avg order > 5000:")
cur.execute("""
SELECT c.city, AVG(o.amount) AS avg_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING AVG(o.amount) > 5000;
""")
for row in cur.fetchall():
    print(row)

conn.close()