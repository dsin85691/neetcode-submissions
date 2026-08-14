CREATE TABLE products (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    price INTEGER
);

INSERT INTO products (name, price) VALUES
('Apple', 5),
('Banana', 7),
('Gift Card', 10),
('Laptop', 1000),
('Phone', 500),
('Pen', 2);
-- Do not modify above this line. --

SELECT SUM(price) as total_discount_price FROM products WHERE price <= 10; 



