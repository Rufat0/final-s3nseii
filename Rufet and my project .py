import mysql.connector 

cnx=mysql.connector.connect(user='root',password='az2001051',host='127.0.0.1',database='isc cedveli i')

database='isc cedveli i'

cursor=cnx.cursor()

cursor.execute("SHOW DATABASES")
for x in cursor:
  print(x)

print(database)
a = int(input("en cox maas alan icini tapmaq ucun 1 yazin,en az maas alan iscini tapmaq ucun 2 yazin ,butun siyahini gostermek ucun 3 yazin"))
if a == 1 :
    cursor.execute('SELECT * FROM `isc cedveli i`.maas')
    for a in cursor:
        print(a)
    cursor.execute("SELECT MAX(Net) AS maximum FROM maas")
    result = cursor.fetchall()
    for i in result:
        print(i[0])
if a == 2 :
    cursor.execute('SELECT * FROM `isc cedveli i`.maas')
    for b in cursor:
        print (b)
    cursor.execute("SELECT MIN(Net) AS minumum FROM maas")
    result = cursor.fetchall()
    for i in result:
        print(i[0])
if a == 3:
    cursor.execute('SELECT * FROM `isc cedveli i`.`ad ve maas`')
    for i in cursor:
        print (i)
