CREATE TABLE unused_table (
  id INTEGER,
  name TEXT
);
-- Do not modify above this line --


DROP TABLE unused_table;




-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'unused_table';
