CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO students (id, name, age) VALUES
(1, 'Alice', 20),
(2, 'Bob', NULL),
(3, 'Charlie', 30);
-- Do not modify above this line. --

UPDATE students SET age = NULL; 



-- Do not modify below this line. --
SELECT * FROM students;
