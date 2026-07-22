CREATE TABLE operating_systems ( 
  id INTEGER PRIMARY KEY, 
  name VARCHAR(255), 
  version CHAR(10), 
  market_share NUMERIC(5,2)
); 







-- Do not modify below this line --
INSERT INTO operating_systems (id, name, version, market_share) VALUES
    (1, 'Windows', '10', 75.51),
    (2, 'macOS', '14.5', 20.12),
    (3, 'Linux', '5.10', 3.75),
    (4, 'Chrome OS', '113', 0.62);

SELECT 
    os.*,
    (SELECT STRING_AGG(column_name || ' ' || data_type || CASE WHEN numeric_precision IS NOT NULL THEN '(' || numeric_precision || ',' || numeric_scale || ')' ELSE '' END, ', ')
     FROM information_schema.columns 
     WHERE table_name = 'operating_systems') AS column_types
FROM 
    operating_systems os;
