CREATE TABLE olympic_medals (
    country TEXT,
    year INTEGER,
    category TEXT,
    gold INTEGER,
    silver INTEGER,
    bronze INTEGER
);

INSERT INTO olympic_medals (country, year, category, gold, silver, bronze) VALUES
    -- 2020 data
    ('USA', 2020, 'Athletics', 12, 15, 10),
    ('China', 2020, 'Athletics', 9, 11, 13),
    ('Japan', 2020, 'Athletics', 7, 9, 11),
    ('Australia', 2020, 'Athletics', 6, 8, 10),
    ('France', 2020, 'Athletics', 5, 7, 9),
    ('Italy', 2020, 'Athletics', 4, 6, 8),
    ('Canada', 2020, 'Athletics', 3, 5, 7),
    
    ('USA', 2020, 'Swimming', 16, 13, 11),
    ('China', 2020, 'Swimming', 10, 12, 9),
    ('Japan', 2020, 'Swimming', 8, 10, 12),
    ('Australia', 2020, 'Swimming', 11, 9, 7),
    ('France', 2020, 'Swimming', 6, 8, 10),
    ('Italy', 2020, 'Swimming', 5, 7, 9),
    ('Canada', 2020, 'Swimming', 4, 6, 8),
    
    ('USA', 2020, 'Gymnastics', 8, 6, 7),
    ('China', 2020, 'Gymnastics', 7, 9, 5),
    ('Japan', 2020, 'Gymnastics', 5, 7, 9),
    ('Australia', 2020, 'Gymnastics', 4, 6, 8),
    ('France', 2020, 'Gymnastics', 3, 5, 7),
    ('Italy', 2020, 'Gymnastics', 2, 4, 6),
    ('Canada', 2020, 'Gymnastics', 1, 3, 5),
    
    -- 2021 data
    ('USA', 2021, 'Athletics', 14, 16, 12),
    ('China', 2021, 'Athletics', 11, 13, 15),
    ('Japan', 2021, 'Athletics', 9, 11, 13),
    ('Australia', 2021, 'Athletics', 8, 10, 12),
    ('France', 2021, 'Athletics', 7, 9, 11),
    ('Italy', 2021, 'Athletics', 6, 8, 10),
    ('Canada', 2021, 'Athletics', 5, 7, 9),
    
    ('USA', 2021, 'Swimming', 18, 15, 13),
    ('China', 2021, 'Swimming', 12, 14, 11),
    ('Japan', 2021, 'Swimming', 10, 12, 14),
    ('Australia', 2021, 'Swimming', 13, 11, 9),
    ('France', 2021, 'Swimming', 8, 10, 12),
    ('Italy', 2021, 'Swimming', 7, 9, 11),
    ('Canada', 2021, 'Swimming', 6, 8, 10),
    
    ('USA', 2021, 'Gymnastics', 10, 8, 9),
    ('China', 2021, 'Gymnastics', 9, 11, 7),
    ('Japan', 2021, 'Gymnastics', 7, 9, 11),
    ('Australia', 2021, 'Gymnastics', 6, 8, 10),
    ('France', 2021, 'Gymnastics', 5, 7, 9),
    ('Italy', 2021, 'Gymnastics', 4, 6, 8),
    ('Canada', 2021, 'Gymnastics', 3, 5, 7);
-- Do not modify above this line. --

SELECT country, year, SUM(gold + silver + bronze) AS total_medals
FROM olympic_medals
WHERE category NOT IN ('Gymnastics')
GROUP BY country, year
HAVING SUM(gold + silver + bronze) > 20
ORDER BY total_medals DESC
LIMIT 5;






