#!/usr/bin/python3
"""script displaying all values of states table

the database name, password and username are passed as arguments.
The handles the user input safely to prevent SQL injection."""
if __name__ == "__main__":
    """prevents code from being imported by other modules."""
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
            port=3306
            )
    cursor = connection.cursor()
    query = f"""
    SELECT * FROM states
    WHERE states.name=%s
    ORDER BY states.id"""
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
    cursor.close()
