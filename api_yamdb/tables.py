
import sqlite3

con = sqlite3.connect('db.sqlite3')


def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())


sql_fetch(con)
