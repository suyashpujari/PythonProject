import MySQLdb
def search():    
        try:
       
                id=int(input("\nEnter the product id:"))
                q="select * from laptops where product_id='%d'" %id
                myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="shopdb")
                cur=myconn.cursor()
                cur.execute(q)
                print("\nExecuted")
                result=cur.fetchall()
                for row in result:
                        print("product Id : ",row[0])
                        print("product Name : ",row[1])
                        print("Price : ",row[2])
        
                myconn.commit() 

        except:
                print("Wrong")
        finally:
                cur.close()
                
                myconn.close()
        