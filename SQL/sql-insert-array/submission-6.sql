CREATE TABLE stocks (
  id INTEGER PRIMARY KEY,
  name TEXT,
  transaction_dates DATE[]
);

-- Do not modify above this line --

INSERT INTO stocks (id, name, transaction_dates) VALUES 
(1, 'AAPL', ARRAY['2007-02-09', '2007-02-10', '2007-02-11']::DATE[]),
(2, 'GOOG', ARRAY['2004-12-15', '2004-12-16']::DATE[]);


-- Do not modify below this line --
SELECT * FROM stocks;