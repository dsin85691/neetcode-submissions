CREATE TABLE events ( 
  id INTEGER PRIMARY KEY, 
  event_date DATE, 
  event_time TIME, 
  event_timestamp TIMESTAMP
); 







-- Do not modify below this line --
INSERT INTO events (id, event_date, event_time, event_timestamp) 
  VALUES (1, '2000-01-01', '12:30:10', '2000-01-01 12:30:10');

SELECT 
    e.*,
    (SELECT STRING_AGG(column_name || ' ' || data_type, ', ')
     FROM information_schema.columns 
     WHERE table_name = 'events') AS column_types
FROM 
    events e;
