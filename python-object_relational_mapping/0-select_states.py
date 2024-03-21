import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
        host = "localhost",
        user = sys.argv[1],
        password = sys.argv[2],
        database = sys.argv[3],
        port = 3306
    )

cur = database.cursor()

req = 'SELECT * FROM states'
cur.execute(req)

citieslist = cur.fetchall()

for city in citieslist:
    print(city)
cur.close()
database.close()
