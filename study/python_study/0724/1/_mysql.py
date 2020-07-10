__author__ = 'mingyu.zhang'
import mysql.connector

conn=mysql.connector.connect(user='root',password='123456',database='working')
cursor=conn.cursor()
#cursor.execute('insert into work_record (num,year,month,day,week,week_num,work_content,work_plan) values (%s,%s,%s,%s,%s,%s,%s,%s)',('395','2019','8','29','四','35','study','null'))
conn.commit()
cursor.execute('select * from work_record where num=%s',('395',))
values=cursor.fetchall()
print(values,cursor.rowcount)
