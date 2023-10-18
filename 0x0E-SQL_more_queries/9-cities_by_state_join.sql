-- script that lists all cities in hbtn_ud_usa
SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id;
