import cx_Oracle as oci
from django.db import connections

conn = oci.connect('system/doosun@localhost:1521/xe')

print(conn.version)

cursor = conn.cursor()
cursor.execute('select*from test_member')
# id로 검색
# sql_select_by_id = 'select * from test_member where id = :mid'
# cursor = conn.cursor()
# cursor.execute(sql_select_by_id, mid='admin')
# print(cursor.fetchone())
# insert
# sql_insert = 'insert into test_member VALUES(test_member_seq.nextVal, :id, :password, :email)'
# cursor.execute(sql_insert, id='kosmo3', password='kosmo31234', email='kosmo3@ikosmo.com')
# conn.commit()
# insert한 내용을 commit
print(cursor.fetchall())
cursor.close()
conn.close