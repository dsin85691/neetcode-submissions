CREATE TABLE athletes (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    sport TEXT
);

INSERT INTO athletes (name, sport) VALUES
  ('LeBron James', 'Basketball'),
  ('Serena Williams', 'Tennis'),
  ('Michael Jordan', 'Basketball'),
  ('Kobe Bryant', 'Basketball'),
  ('Cristiano Ronaldo', 'Soccer'),
  ('Lionel Messi', 'Soccer'),
  ('Tom Brady', 'Football'),
  ('Usain Bolt', 'Track and Field');
-- Do not modify above this line. --

SELECT name FROM athletes WHERE sport <> 'Basketball'; 



