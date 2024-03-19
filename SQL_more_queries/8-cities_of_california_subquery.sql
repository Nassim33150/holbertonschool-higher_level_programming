-- Select id and name  from the 'cities' table in the 'hbtn_0d_usa' database
-- Order the results by the 'id' column in ascending order
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id;
