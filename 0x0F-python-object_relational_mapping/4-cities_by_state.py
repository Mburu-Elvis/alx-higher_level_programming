#!/usr/bin/python3
"""a script taking 3 arguments.

the module then lists all cities from a database."""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """the condition prevents the code from being imported."""
    username = argv[1]
    pwd = argv[2]
    db = argv[3]
    connection = MySQLdb.connect(
            user=username,
            password=pwd,
            database=db,
            port=3306,
            host='localhost'
            )
    cursor = connection.cursor()
    query = f"""
    SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states
    ON states.id=cities.state_id
    ORDER BY cities.id
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}', '{row[2]}')")
    cursor.close()
