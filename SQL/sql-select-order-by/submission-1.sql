CREATE TABLE comments (
    id INT PRIMARY KEY,
    author TEXT,
    body TEXT,
    created_at TIMESTAMP
);

INSERT INTO comments (id, author, body, created_at) VALUES
(1, 'NeetCode', 'My first comment', '2022-07-11 10:00:00'),
(2, 'Lee', 'Another comment', '2019-02-14 10:01:00'),
(3, 'NeetCode', 'My second comment', '2022-08-01 10:02:00'),
(4, 'John', 'This is another comment', '2021-12-24 10:03:00');
-- Do not modify above this line. --

SELECT author, body, created_at FROM comments ORDER BY created_at DESC;



