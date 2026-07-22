
CREATE TABLE products ( 
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    price INTEGER CHECK (price >= 0), 
    status TEXT CHECK (status IN ('available', 'out of stock'))
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
    COALESCE(chk.check_clause, 'NO') AS check_constraint
FROM 
    information_schema.columns c
LEFT JOIN (
    SELECT kcu.table_name, kcu.column_name
    FROM information_schema.key_column_usage kcu
    JOIN information_schema.table_constraints tc
        ON kcu.constraint_name = tc.constraint_name
        AND tc.constraint_type = 'PRIMARY KEY'
) pk ON c.table_name = pk.table_name AND c.column_name = pk.column_name
LEFT JOIN (
    SELECT ccu.table_name, ccu.column_name, 
           pg_get_constraintdef(con.oid) AS check_clause
    FROM pg_constraint con
    JOIN pg_namespace nsp ON nsp.oid = con.connamespace
    JOIN pg_class cls ON cls.oid = con.conrelid
    JOIN information_schema.constraint_column_usage ccu
        ON con.conname = ccu.constraint_name
        AND nsp.nspname = ccu.table_schema
        AND cls.relname = ccu.table_name
    WHERE con.contype = 'c'
) chk ON c.table_name = chk.table_name AND c.column_name = chk.column_name
WHERE 
    c.table_name = 'products'
ORDER BY 
    c.ordinal_position;
