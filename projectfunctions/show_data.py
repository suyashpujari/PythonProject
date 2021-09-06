import MySQLdb
def show():
        try:
                q="select * from laptops"
                myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="shopdb")
                cur=myconn.cursor()
                cur.execute(q)
                #print("executed")
                result=cur.fetchall()
                for rows in result:
                        print(rows[0],") product Id : ",rows[0])
                        print("  product Name : ",rows[1])
                        print("  Price : ",rows[2],"\n")
                myconn.commit()   
        except:
                if myconn != None:
                        myconn.rollback()
                        print("Database connection has some issues")
        finally:
                cur.close()
                myconn.close()