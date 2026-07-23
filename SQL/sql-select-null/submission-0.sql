CREATE TABLE comments (
    id INT PRIMARY KEY,
    author TEXT,
    body TEXT
);

INSERT INTO comments (id, author, body) VALUES
(1, 'NeetCode', 'This problem should be marked as easy.. haha'),
(2, 'Lee', 'This problem is too hard for an easy tag'),
(3, NULL, 'This is a test comment'),
(4, 'John', 'This is another test comment'),
(5, NULL, 'This is a test comment with NULL author');
-- Do not modify above this line. --



SELECT * FROM comments WHERE author IS NOT NULL;