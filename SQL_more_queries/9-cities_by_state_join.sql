SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.states
INNER JOIN cities ON states.id = cities.state_id
ORDER BY cities.id ASC;
