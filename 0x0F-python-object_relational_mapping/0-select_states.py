#!/usr/bin/python3
"""script that lists all states from the database"""


if __name__ == '__main__':
    """makes the code not execute when imported"""
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=username, password=password, database=database)
    c = db.cursor()
    c.execute("""SELECT id, name FROM states ORDER BY states.id ASC""")
    rows = c.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
        c.close()
