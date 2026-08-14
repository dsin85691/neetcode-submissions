CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO students (id, name)
  VALUES (1, 'Alice'),
         (2, 'Bob'),
         (3, 'Charlie');
-- Do not modify above this line. --


TRUNCATE TABLE students; 



-- Do not modify below this line. --
SELECT * FROM students;
