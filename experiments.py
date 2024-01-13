import pypika
import sqlite3
from pypika import functions as fn, Table

import pandas as pd


sqlite_con = sqlite3.connect(":memory:")
cursor = sqlite_con.cursor()

cursor.execute("CREATE TABLE t1(id, id2, string1)")
cursor.execute("CREATE TABLE t2(id, id2, string1)")

data1 = [
    (1, 1, "11"),
    (2, 1, "21"),
    (3, 2, "32")
]

data2 = [
    (1, 3, "13"),
    (2, 1, "21"),
    (3, 2, "32")
]

cursor.executemany("INSERT INTO t1 VALUES(?, ?, ?)", data1)
cursor.executemany("INSERT INTO t2 VALUES(?, ?, ?)", data2)

a = pd.read_sql(
    str(pypika.Query
            .from_("t1")
            .select('*')
            .limit(3)),
    sqlite_con
)

t1 = Table('t1')

pd.read_sql(
    str(pypika.Query\
        .from_(t1)\
        .groupby(t1.id2)\
        .select(t1.id2, fn.Sum(t1.id))),
    sqlite_con
)

class MyTable(pypika.queries.QueryBuilder):
    def __init__(self, connection, table_name):
        self.QueryBuilder = pypika.Query
        self.table_name = table_name
        self.connection = connection  # self.from_(t1)

    def __repr__(self):
        return(pd.read_sql(
            str(self.select("*").limit(10)),
            self.connection
        ).__repr__())
    
    def getTable(self, table_name):
        self.QueryBuilder.from_(table_name)
        return self
    

tbl = MyTable(sqlite_con).getTable( table_name="t1")
tbl

tbl.from_("t1").select("id")

## Goal:
## >>> tbl
## Now works:
## >>> tbl.form_("t1")


pypika.Query.from_("t1").select("id")

tbl.select("id2")

print(pypika.Query\
        .from_(t1)\
        .groupby(t1.id2)\
        .select(t1.id2, fn.Sum(t1.id)))

str(tbl)
