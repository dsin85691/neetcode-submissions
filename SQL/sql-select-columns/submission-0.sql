CREATE TABLE comments (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    author TEXT,
    body TEXT,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO comments (author, body) VALUES
    ('NeetCode', 'This problem should be marked as easy.. haha'),
    ('Lee', 'This problem is too hard for an easy tag');
-- Do not modify above this line. --


SELECT author AS comment_author, body AS comment_body FROM comments; 

