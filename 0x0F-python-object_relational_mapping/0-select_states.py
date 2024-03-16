#!/usr/bin/python3

"""A script that lists all states from the database named hbtn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    mydb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    mmydb.close()
