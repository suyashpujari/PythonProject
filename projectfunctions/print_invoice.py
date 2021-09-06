import MySQLdb
def invoice():
    print ("\nENTER THE PRODUCT ID OF PRODUCT U WANT TO BYE:")
    id=int (input())
    try:
        q="select * from laptops where product_id='%d'" %id
        myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="shopdb")
        cur=myconn.cursor()
        cur.execute(q)
        result=cur.fetchall()
        
        for rows in result:
            
            print("-----------------------WELCOME TO NEW TECH COMPUTERS----------------- \n \t\t1562,lane no.5 off parola road,Jalgoan,424001")
            print("PHONE NO:(02565)\t\t\tGSTIN:27AEAPTO162J12ZI")
            print("____________________________________________________________________")
            print("\n")
            print("PRODUCT _ID:",rows[0])
            print("\n")
            print("PRODUCT_NAME:",rows[1])
            print("\n")
            print("PRICE:",rows[2])
            print("\n")
            print("---------------THANK YOU FOR PURCHASING VISIT AGAIN :)-------------------")          
    
        myconn.commit()
    except:
         if myconn != None:
                        myconn.rollback()
                        print("Database connection has some issues")
                        print("Something Wrong :(")


    finally:
        print("\nPLZ CONFORM YOUR PURCHASE  \n yes=1 \tno=2")
        if int(input()!=1):
            print("\nPURCHASE SUCCESSFUL THANK YOU.........")
        else:
            print("\nPURCHASE UNSUCESSFUL PLZ TRY AGIAN...")