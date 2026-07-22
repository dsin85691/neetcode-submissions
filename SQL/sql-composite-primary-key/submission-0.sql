CREATE TABLE orders ( 
    order_id INTEGER, 
    product_id INTEGER, 
    quantity INTEGER, 
    PRIMARY KEY (order_id, product_id)
); 






-- Do not modify below this line --
SELECT 
    c.table_name,
    c.column_name, 
    c.data_type, 
    CASE 
        WHEN kcu.column_name IS NOT NULL THEN 
            CASE 
                WHEN COUNT(*) OVER (PARTITION BY kcu.constraint_name) > 1 THEN 'YES (Composite)'
                ELSE 'YES'
            END
        ELSE 'NO'
    END AS is_primary_key
FROM 
    information_schema.columns c
LEFT JOIN 
    information_schema.key_column_usage kcu
    ON c.table_name = kcu.table_name 
    AND c.column_name = kcu.column_name
LEFT JOIN 
    information_schema.table_constraints tc
    ON kcu.constraint_name = tc.constraint_name
    AND tc.constraint_type = 'PRIMARY KEY'
WHERE 
    c.table_name = 'orders'
ORDER BY 
    c.ordinal_position;
