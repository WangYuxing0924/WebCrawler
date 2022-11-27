import pymysql
def getconnector():
   db = pymysql.connect(host="localhost", user="root",
                             password="A7k7SkHm!xd*", db="flight", port=3306)
   return db


def mysqlQuery(tableName):
    db = getconnector()
    sql = "select * from "+tableName
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句

        results = cur.fetchall()  # 获取查询的所有记录
        print("flightno", "departtime", "departairport", "departterminal")
        print("results:"+str(len(results)))
        # 遍历结果
        for row in results:
            flightno = row[0]
            departtime = row[1]
            departairport = row[2]
            departterminal = row[3]
            print(flightno, departtime, departairport, departterminal)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接

def mysqlInsert(tableName, flight_list):
    import pymysql
    # 2.插入操作
    db = getconnector()
    try:
        for flight in flight_list:
            cur = db.cursor()
            flightno = flight.get("flight_no")

            departtime = flight.get("depart_time")
            departairport = flight.get("depart_airport")
            departterminal = flight.get("depart_terminal")
            arrivetime = flight.get("arrive_time")
            arriveairPort = flight.get("arrive_airPort")
            arriveterminal = flight.get("arrive_terminal")
            status = flight.get("status_green")
            print("flightno=====" + flightno+" departtime:"+departtime+" departairport:"+departairport+" departterminal:"+departterminal+" arrivetime:"+arrivetime+" arriveairPort:"+arriveairPort+" arriveterminal:"+arriveterminal+" status:"+status)
            #sql_insert = "insert into flight.flight(flightno,departtime,departairport,departterminal,arrivetime,arriveairport,arriveterminal,status) values('"+flightno+"','"+departtime+"','"+departairport+"','"+departterminal+"','"+arrivetime+"','"+arriveairPort+"','"+arriveterminal+"','"+status+"')"
            sql_insert = "insert into "+tableName+"(flightno,departtime,departairport,departterminal,arrivetime,arriveairport,arriveterminal,status) values('"+flightno+"','"+departtime+"','"+departairport+"','"+departterminal+"','"+arrivetime+"','"+arriveairPort+"','"+arriveterminal+"','"+status+"')"

            #sql_insert = "insert into flight.flight(flightno,departtime,departairport,departterminal,arrivetime,arriveairport,arriveterminal,status) values('1111','bbbb','cccc','ddd','eee','fff','ggg','hhhh')"
            #sql_insert = "insert into my(name,age) values('"+"aaaassz"+"','"+status+"')"

            try:
                cur.execute(sql_insert)
                # 提交
                #db.commit()
            except Exception as e:
                # 错误回滚
                print(e)
                #db.rollback()
            # finally:
            #     db.close()
        db.commit()
    except Exception as er:
        print(er)

def mysqlDelete(tableName):
    db = getconnector()
    cur = db.cursor()
    sql_delete = "delete from "+tableName
    try:
        cur.execute(sql_delete)  # 像sql语句传递参数
        # 提交
        db.commit()
    except Exception as e:
        # 错误回滚
        db.rollback()
    finally:
        db.close()

def createTable(tableName):
    db = getconnector()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS "+tableName)

    # 创建student表
    sql = """
            CREATE TABLE `"""+tableName+"""` (
          `flightno` varchar(45) NOT NULL,
          `departtime` varchar(45) DEFAULT NULL,
          `departairport` varchar(45) DEFAULT NULL,
          `departterminal` varchar(45) DEFAULT NULL,
          `arrivetime` varchar(45) DEFAULT NULL,
          `arriveairport` varchar(45) DEFAULT NULL,
          `arriveterminal` varchar(45) DEFAULT NULL,
          `status` varchar(45) DEFAULT NULL,
          PRIMARY KEY (`flightno`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
        """

    try:
        # 执行SQL语句
        cursor.execute(sql)
        print("创建数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s" % e)
    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()