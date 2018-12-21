import sqlite3

## test SQlLIGHT
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('drop table users')
create_table='create table users(id  INTEGER PRIMARY KEY AUTOINCREMENT,username text,password text )'
cursor.execute(create_table)
users=[
    (1,'satej','sarker'),
    (2,'samir','sarker')
]

insert_qurry='insert into users values(?,?,?)'
cursor.executemany(insert_qurry,users)
select_qury = 'select * from users'
for row in cursor.execute(select_qury):
    print(row)


connection.commit()
connection.close()