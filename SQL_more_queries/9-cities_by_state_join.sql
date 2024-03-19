-- Select the id and name columns from the 'cities' table, and the name column from the 'states' table
-- Join the 'cities' table with the 'states' table based on the 'id' and 'state_id' columns, respectively
-- Order the results by the 'id' column of the 'cities' table in ascending order
SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id
