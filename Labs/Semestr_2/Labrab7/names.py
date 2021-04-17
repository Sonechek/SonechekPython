import pymysql.cursors

conn = pymysql.connect(
    host='localhost',
    user='soft0049',
    password='tWpds59l',
    db='soft0049_labrab',
    port=1500,
    cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

sql = "SElECT * FROM students WHERE city = Кунгур"
cur.execute(sql, id)
row = cur.fetchone()
print(row)

conn.close()
