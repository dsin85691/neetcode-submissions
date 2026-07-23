CREATE TABLE cities (
    id INT PRIMARY KEY,
    name TEXT,
    country TEXT,
    population INTEGER
);

INSERT INTO cities (id, name, country, population) VALUES
(1, 'Tokyo', 'Japan', 37400068),
(2, 'London', 'England', 8982000),
(3, 'Paris', 'France', 2141000),
(4, 'New York', 'USA', 8419000),
(5, 'New Delhi', 'India', 19640000),
(6, 'Shanghai', 'China', 25700000),
(7, 'Sao Paulo', 'Brazil', 12330000),
(8, 'Mexico City', 'Mexico', 8918000),
(9, 'Cairo', 'Egypt', 20010000),
(10, 'Mumbai', 'India', 20660000),
(11, 'Beijing', 'China', 21540000),
(12, 'Los Angeles', 'USA', 3971000),
(13, 'Chicago', 'USA', 2716000),
(14, 'Manila', 'Philippines', 13160000),
(15, 'Moscow', 'Russia', 12610000),
(16, 'Istanbul', 'Turkey', 15580000),
(17, 'Kolkata', 'India', 14780000),
(18, 'Bangkok', 'Thailand', 8305000),
(19, 'Jakarta', 'Indonesia', 10560000),
(20, 'Lahore', 'Pakistan', 11120000),
(21, 'Chengdu', 'China', 14040000);
-- Do not modify above this line. --

SELECT name FROM cities WHERE population < 1000000 or population > 10000000 AND name NOT LIKE 'C%';




