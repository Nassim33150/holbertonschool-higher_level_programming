-- Select the id and name columns from the 'cities' table, and the name column from the 'states' table
-- Join the 'cities' table with the 'states' table based on the 'id' and 'state_id' columns, respectively
-- Order the results by the 'id' column of the 'cities' table in ascending order
SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.states
INNER JOIN cities ON states.id = cities.state_id
ORDER BY cities.id ASC;
