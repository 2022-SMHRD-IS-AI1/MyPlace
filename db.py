import cx_Oracle

def login_check(id,pw):
    if not cx_Oracle.init_oracle_client:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\777\Oracle\instantclient_21_9")

    try:
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        conn = cx_Oracle.connect('kgt1234','123456a','project-db-stu.ddns.net:1524/xe', encoding="UTF-8")

        cursor = conn.cursor()

        conn = cx_Oracle.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM MY_USER WHERE USER_ID = %s AND USER_PW = %s"% (id, pw)
        value = (id, pw)
        cursor.execute("set names utf8")
        cursor.execute(sql, value)

        data = cursor.fetchall()
    except:
        print('invalid input data detected !')
    finally:
        cursor.close()
        conn.close()
        
    return data

def join(id,pw,email):
    if not cx_Oracle.init_oracle_client:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\777\Oracle\instantclient_21_9")

    try:
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        conn = cx_Oracle.connect('kgt1234','123456a','project-db-stu.ddns.net:1524/xe', encoding="UTF-8")

        cursor = conn.cursor()

        conn = cx_Oracle.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO MY_USER VALUES ('%s', '%s', '%s')" % (id, pw, email)
        value = (id, pw)
        cursor.execute("set names utf8")
        cursor.execute(sql, value)

        data = cursor.fetchall()
        if not data:
            conn.commit()
        else:
            conn.rollback()
    except:
        conn.rollback()
        print('invalid input data detected !')
    finally:
        cursor.close()
        conn.close()
        
    return data
        
    
    