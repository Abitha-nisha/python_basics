# dummy=open("abi.txt","w")
# dummy.write("Hi Abitha welcome  to vglug")
# dummy.write("\nwhat learn today?")
# dummy.write("\n i learned today fact check")
# dummy.close()

# Python program to illustrate
# Append vs write mode
# file1 = open("demo.txt", "w")
# L =["kasi\n","saritha\n","abii\n","sakthi\n"]
# file1.writelines(L)
# file1.close()

# # Append-adds at last
# file1 = open("abifile.txt", "a")  # append mode
# file1.write("Today is very funy \n")
# file1.close()

# file1 = open("abifile.txt", "r")
# # print("Output of Readlines after appending")
# print(file1.readlines())
# # print()
# file1.close()

# # # Write-Overwrites
# file1 = open("abifile.txt", "w")  # write mode
# file1.write("Tomorrow is filehandling i am finshing\n")
# file1.write('today i am llearning in file hndling')
# file1.close()

# file1 = open("abifile.txt", "r")
# print("Output of Readlines after writing")
# print(file1.readlines())
# print()
# file1.close()

#wite
# file1=open("abifile.txt",'w')
# file1.write("welocme to our home")
# file1.write(" is always special")
           
#writelines
# file=open("abi.txt",'r')
# print(file.readlines())

#append
# f=open("abifile.txt",'a')
# f.write("hii welcome to vglug")
# f.write("vglg foundation created more software employye")

# #read
# file=open("demo.txt",'r')
# print(file.read())

# #readlines
# fi=open("demo.txt",'r')
# # print(fi.readline())
# # print(fi.readline())
# for i in fi:
#     print(i.strip())

# f=open("demo.txt","r")
# print(f.read(3))
# print(f.read())

# f=open("abi.txt","a")
# f.write("great")

# try:
#     file=open("abio.txt","r")
#     print(file.read())
# except FileNotFoundError:
#     print("error: file not found ")
# else:
#     file.close()

# f=open("abifile.txt","r")
# print(f.readline())
# print(f.readline(27))

# f=open("abifile.txt","r")
# print(f.readlines())

# file=open("abifile.txt","r")
# for i in file:
#     print(i)

# f=open("abi.txt","w")
# f.write("hi my name is abitha ")
# f.close()
# f=open("abi.txt","r")
# for k in f:
#     print(k)

# f=open("abi.txt","a")
# f.write("i am coming from thirukkovilur ")
# f.close()
# f=open("abi.txt","r")
# print(f.read())

# import os
# if os.path.exists("book.stored.txt"):
#     os.remove("book.stored.txt")
# else:
#     print("file not")


