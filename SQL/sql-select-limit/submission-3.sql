CREATE TABLE flights (
    id INT PRIMARY KEY,
    origin TEXT ,
    destination TEXT,
    price INT
);

INSERT INTO flights (id, origin, destination, price) VALUES
(1, 'London', 'Paris', 100),
(2, 'Paris', 'London', 150),
(3, 'Berlin', 'London', 200),
(4, 'London', 'Berlin', 120),
(5, 'Paris', 'Berlin', 110),
(6, 'Berlin', 'Paris', 130),
(7, 'London', 'Paris', 90),
(8, 'Paris', 'London', 140),
(9, 'Berlin', 'London', 180),
(10, 'London', 'Berlin', 115),
(11, 'London', 'Paris', 105),
(12, 'Paris', 'London', 160),
(13, 'Berlin', 'London', 210),
(14, 'London', 'Paris', 125),
(15, 'Paris', 'Berlin', 115);
-- Do not modify above this line. --

SELECT * FROM flights WHERE origin = 'London' AND destination = 'Paris' ORDER BY price ASC LIMIT 2; 







