#!/usr/bin/python3
"""script taking arguments, displays all values in states matching name arg."""

if __name__ == '__main__':
    """prevents importion of code by other modules."""
    import MySQLdb
    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]
    connection = MySQLdb.connect(
            user=username,
            password=password,
            database=database,
            host='localhost',
            port=3306)
    cursor = connection.cursor()
    query = """
    SELECT * FROM states
    WHERE states.name = '{}'
    ORDER BY states.id ASC""".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
    cursor.close()
