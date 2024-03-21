import MySQLdb

mydb = MySQLdb.connect(
    user = 'root',
    password = 'root',
    database = 'hbtn_0e_0_usa',
    host = 'localhost'
)

cur = mydb.cursor()

req = 'SELECT * FROM states'
cur.execute(req)

citieslist = cur.fetchall()

for city in citieslist:
    print(city)
