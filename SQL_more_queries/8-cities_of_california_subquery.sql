-- Select id and name  from the 'cities' table in the 'hbtn_0d_usa' database
-- Order the results by the 'id' column in ascending order
SELECT id, name FROM hbtn_0d_usa.cities
WHERE state_id = 1
ORDER BY cities.id ASC;
