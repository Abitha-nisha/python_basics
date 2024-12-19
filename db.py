# import sqlite3
# con=sqlite3.connect("db_pro/users")

# def insertData(name,age,city):
#     qry="insert into users(NAME,AGE,CITY) values (?,?,?);"
#     con.execute(qry,(name,age,city))
#     con.commit()
#     print("user details added")
    
# def updatetData(name,age,city,id):
#     qry="update users set Name=?,AGE=?,CITY=? where id=?;"
#     con.execute(qry,(name,age,city))
#     con.commit()
#     print("user details updated")
    
# print("""
# 1.Insert
# 2.Update
# 3.Delete
# 4.Select
# """)

# ch=1
# while ch==1:
#     c=int(input("Select your choice:"))
#     if (c==1):
#          print("Add new record")
#          name=input("Enter name:")
#          age=input("Enter age:")
#          city=input("Enter city:")
#          insertData(name,age,city)
#     elif (c==2):
#          print("Edit a record")
#          id=input("Enter id:")
#          name=input("Enter name:")
#          age=input("Enter age:")
#          city=input("Enter city:")
#          updatetData(name,age,city,id)
#     elif (c==3):
#          print("Dlete a record")
#     elif (c==4):
#          print("print all record")
#     else:
#          print("Invalid select")
#     ch=int(input("Enter 1 to continue:"))
# print("thank you")

