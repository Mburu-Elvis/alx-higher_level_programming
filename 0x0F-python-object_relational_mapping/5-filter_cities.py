#!/usr/bin/python3
"""script that takes 4 arguments

it lists all the cities filtered by state"""


if __name__ == "__main__":
    """prevents the code from being imported."""
    import MySQLdb
    from sys import argv

    username = argv[1]
    pwd = argv[2]
    db = argv[3]
    state_name = argv[4]
    connection = MySQLdb.connect(
            user=username,
            password=pwd,
            database=db,
            port=3306,
            host='localhost'
            )
    cursor = connection.cursor()
    query = f"""
    SELECT cities.name FROM cities
    INNER JOIN states
    ON states.id=cities.state_id
    WHERE states.name='%s'
    ORDER BY cities.id ASC
    """ % (state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    i = 0
    for row in rows:
        if i < (len(rows) - 1):
            print(f"{row[0]}, ", end="")
        else:
            print(row[0])
        i += 1
