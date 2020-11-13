from sqlalchemy import create_engine

db_uri = "sqlite:///db.sqlite"
engine = create_engine(db_uri)

# DBAPI - PEP249
# create table

#engine.execute('CREATE TABLE "EX1" ('
#               'id INTEGER NOT NULL,'
#               'name VARCHAR, '
#               'PRIMARY KEY (id));')

# insert a raw
engine.execute('INSERT INTO "EX1" '
               '(id, name) '
               'VALUES (' ',"raw1")')

# select *
result = engine.execute('SELECT * FROM '
                        '"EX1"')
for _r in result:
   print(_r)

# delete *
#engine.execute('DELETE from "EX1" where id=1;')
#result = engine.execute('SELECT * FROM "EX1"')
#print(result.fetchall())