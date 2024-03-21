#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""
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

    state = sys.argv[4]

    req = "SELECT cities.name FROM cities " \
        "JOIN states ON cities.state_id = states.id " \
        "WHERE states.name = %s ORDER BY cities.id ASC"

    cur.execute(req, (state,))

    citieslist = cur.fetchall()

    city_names = []

    for city in citieslist:
        city_names.append(city[0])
    print(", ".join(city_names))
    cur.close()
    database.close()
