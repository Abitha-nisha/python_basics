# import sqlite3
# con=sqlite3.connect("data_pr")

# def insertData (name,age,city):
#     qry="insert into data_pr (NAME,AGE,CITY) values (?,?,?);"
#     con.execute(qry,(name,age,city))
#     con.commit()
#     print("user Details added")
    
# print("""
# 1.Insert
# 2.Update
# 3.Delete
# 4.Select
# """)

# ch=1
# while ch==1:
#     c=int(input("Select your choice:"))
#     if(c==1):
#          print("Add new record")
#          name=input("enter name:")
#          age=int(input("enter age:"))
#          city=input("enter city:")
#          insertData (name,age,city)
#     elif (c==2):
#          print("Edit a record")
#     elif (c==3):
#          print("Delete a record")
#     elif (c==4):
#          print("print all record")
#     else:
#         print("invalid selection")
#     ch=int(input("Enter 1 to continue:"))
# print("thank you")

