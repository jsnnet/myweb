import cx_Oracle as oci

conn = oci.connect('doosun/doosun@localhost:1521/xe')

print(conn.version)

cursor = conn.cursor()
cursor.execute('select*from test_member')
print(cursor.fetchall())

cursor.close()
conn.close