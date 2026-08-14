CREATE TABLE students (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    age INTEGER
);

INSERT INTO students (name, age)
  VALUES ('John Doe', 20),
         ('Jane Doe', 21),
         ('John Smith', 22),
         ('Jane Smith', 23);
-- Do not modify above this line. --


DELETE FROM students; 


-- Do not modify below this line. --
SELECT * FROM students;
