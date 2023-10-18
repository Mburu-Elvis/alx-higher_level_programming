-- script listing all cities in California in hbtn_0d_usa database
SELECT id, name FROM cities WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name='California') ORDER BY cities.id;
