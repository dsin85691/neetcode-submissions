CREATE TABLE students (
    id INT PRIMARY KEY,
    name TEXT
);

CREATE TABLE course_registrations (
    id INT PRIMARY KEY,
    student_id INT,
    course_name TEXT
);

INSERT INTO students (id, name) VALUES
(1, 'Adam Smith'),
(2, 'Thomas Jefferson'),
(3, 'John Adams'),
(4, 'James Madison');

INSERT INTO course_registrations (id, student_id, course_name) VALUES
(1, 1, 'Math'),
(2, 1, 'Science'),
(3, 2, 'Math'),
(4, 2, 'History'),
(5, 3, 'Science'),
(6, 3, 'Math'),
(7, 4, 'History'),
(8, 4, 'Math');
-- Do not modify above this line. --

SELECT name, course_name FROM students INNER JOIN course_registrations ON students.id = student_id ORDER BY name ASC;  




