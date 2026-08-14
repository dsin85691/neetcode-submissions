CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    class_id INTEGER REFERENCES classes(id)
);

INSERT INTO classes (id, name) VALUES (1, 'Math');
INSERT INTO students (id, name) VALUES (1, 'Alice');
INSERT INTO enrollments (id, student_id, class_id) VALUES (1, 1, 1);
-- Do not modify above this line. --

DELETE FROM enrollments;
DELETE FROM classes;
DELETE FROM students;


-- Do not modify below this line. --
SELECT * FROM enrollments;
