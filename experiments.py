import pypika
import sqlite3

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


cursor.execute(str(pypika.Query.from_("t1").select('*'))).fetchall()



pd.read_sql(
    str(pypika.Query
            .from_("t1")
            .select('*')
            .limit(1)
        ),
    sqlite_con
)


