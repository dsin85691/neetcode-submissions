CREATE TABLE coding_problems (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    difficulty TEXT,
    description TEXT
);

INSERT INTO coding_problems (name, difficulty, description) VALUES
    ('Dynamic Array', 'Easy', 'Implement a dynamic array in C++'),
    ('Binary Search Tree', 'Medium', 'Implement a binary search tree in C++'),
    ('Graph Traversal', 'Hard', 'Implement depth-first search and breadth-first search in C++');
-- Do not modify above this line. --

SELECT * from coding_problems; 
