import MySQLdb
def delete():
        try:
                print("\nEnter the product id:")
                id=int(input())
                q="delete from laptops where product_id='%d'" %id
                myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="shopdb")
                cur=myconn.cursor()
                cur.execute(q)
        
                myconn.commit()   
        except:
                if myconn != None:
                        myconn.rollback()
                        print("Database connection has some issues")
        finally:
                cur.close()
                myconn.close()
        

