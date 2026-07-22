CREATE TABLE departments ( 
  id INTEGER PRIMARY KEY, 
  name TEXT
); 


CREATE TABLE employees ( 
  id INTEGER PRIMARY KEY, 
  name TEXT, 
  department_Id INTEGER REFERENCES departments(id)
); 









-- Do not modify below this line --
SELECT 
    c.table_name,
    c.column_name, 
    c.data_type,
    CASE 
        WHEN pk.column_name IS NOT NULL THEN 'YES'
        ELSE 'NO'
    END AS is_primary_key,
    CASE 
        WHEN fk.column_name IS NOT NULL THEN 
            'YES (References ' || fk.foreign_table_name || '.' || fk.foreign_column_name || ')'
        ELSE 'NO'
    END AS is_foreign_key
FROM 
    information_schema.columns c
LEFT JOIN (
    SELECT kcu.table_name, kcu.column_name
    FROM information_schema.key_column_usage kcu
    JOIN information_schema.table_constraints tc 
        ON kcu.constraint_name = tc.constraint_name
    WHERE tc.constraint_type = 'PRIMARY KEY'
) pk ON c.table_name = pk.table_name AND c.column_name = pk.column_name
LEFT JOIN (
    SELECT 
        kcu.table_name, 
        kcu.column_name, 
        ccu.table_name AS foreign_table_name,
        ccu.column_name AS foreign_column_name
    FROM information_schema.key_column_usage kcu
    JOIN information_schema.referential_constraints rc 
        ON kcu.constraint_name = rc.constraint_name
    JOIN information_schema.constraint_column_usage ccu 
        ON rc.unique_constraint_name = ccu.constraint_name
) fk ON c.table_name = fk.table_name AND c.column_name = fk.column_name
WHERE 
    c.table_name IN ('departments', 'employees')
ORDER BY 
    c.table_name,
    c.ordinal_position;
