#!/usr/bin/python3
""" takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name
matches the argument. """
import MySQLdb
import sys

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    cur = database.cursor()

    req = "SELECT id, name FROM cities ORDER BY cities.id ASC"

    cur.execute(req)

    citieslist = cur.fetchall()

    for city in citieslist:
        print(city)
    cur.close()
    database.close()
