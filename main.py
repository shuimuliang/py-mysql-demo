import mysql.connector

def main():
    conn = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='foo')

    cursor = conn.cursor()

    query = ("SELECT d, dau, r1, r2, r3, r4, r5 from active_user_report")

    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

    conn.close()

if __name__ == '__main__':
    main() 

