import cx_Oracle

def login_check(id, pw):
    try:
        if not cx_Oracle.init_oracle_client:
            cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_9")
        
        conn = cx_Oracle.connect('kgt1234', '123456a', 'project-db-stu.ddns.net:1524/xe', encoding="UTF-8")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM MY_USER WHERE USER_ID = (:1) AND USER_PW = (:2)", [id, pw])

        data = cursor.fetchall()
    except cx_Oracle.Error as error:
        print('Oracle database error:', error)
        data = None
    except Exception as exception:
        print('Error occurred:', exception)
        data = None
    finally:
        cursor.close()
        conn.close()

    return data

def join(id,pw,email):
    if not cx_Oracle.init_oracle_client:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_9")
    result = 0
    #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
    conn = cx_Oracle.connect('kgt1234','123456a','project-db-stu.ddns.net:1524/xe', encoding="UTF-8")
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO MY_USER VALUES ('%s', '%s', '%s')" % (id, pw, email))
        conn.commit()
        result = 1
        
    except:
        print('invalid input data detected !')
    finally:
        cursor.close()
        conn.close()
        
    return result
        
    
    