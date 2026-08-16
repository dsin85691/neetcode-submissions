CREATE TABLE products (
    product_id INTEGER,
    product_name TEXT,
    store_name TEXT
);

INSERT INTO products (product_id, product_name, store_name) VALUES
    (1, 'Laptop', 'Amazon'),
    (2, 'Phone', 'Best Buy'),
    (3, 'Tablet', 'Walmart'),
    (4, 'Laptop', 'Amazon'),
    (5, 'Phone', 'Best Buy'),
    (6, 'Tablet', 'Walmart'),
    (7, 'Laptop', 'Amazon'),
    (8, 'Washing Machine', 'Best Buy'),
    (9, 'Laptop', 'Walmart'),
    (10, 'Phone', 'Amazon');
-- Do not modify above this line. --


SELECT product_name, store_name FROM products GROUP BY product_name, store_name ORDER BY product_name, store_name ASC; 


