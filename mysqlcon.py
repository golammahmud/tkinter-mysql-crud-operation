import pymysql

con = pymysql.connect(
		host='localhost',
		user='root',
		password = "",
		db='student',
		)

try:

    # with con.cursor() as cur:
    #
    #     cur.execute('SELECT VERSION()')
    #
    #     version = cur.fetchone()
    #
    #     print(f'Database version: {version[0]}')
    with con.cursor() as cur:

        cur.execute('SELECT * FROM student_profile')

        rows = cur.fetchall()

        # for row in rows:
        #     print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
        for row in rows:
            print((row['id'], row['name']))

finally:

    con.close()