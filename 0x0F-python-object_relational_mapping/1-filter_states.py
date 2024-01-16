#!/usr/bin/python3
"""script that lists all states with a name starting with N,

from database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """prevents the code from being imported"""
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    connection = MySQLdb.connect(
            user=username,
            password=password,
            database=database,
            host='localhost',
            port=3306
        )
    query = "SELECT * FROM states WHERE states.name LIKE 'N%'"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
    cursor.close()
