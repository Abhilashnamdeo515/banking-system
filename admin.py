import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",
                  passwd="Abhi@4321",database="employeemanagement")
cur=con.cursor()

#============================================================================================

def cr1():
   q="create table auth1(userid char(30),pass1 char(30))"
   cur.execute(q)
   con.commit()

#============================================================================================

def incr1(): # parameterized argument
   user_id=input("☞ enter your user id ")
   pas=input("enter your password ")
   t=(user_id,pas)
   q="insert into auth1 values(%s,%s)"
   cur.execute(q,t)
   con.commit()
   print("data stored")

#============================================================================================

def authcheck():
    print()
    print(" "*102," ⬇⬇️")
    print()
    print(" "*101,"☾ 웃 ☽")
    print(" "*101," ●●●●")
    print(" "*79," ----------- You Need To LOG-IN First ----------- ")
    print()
    user_id=input("                                                                                          => Enter Your User- ID : ")
    pas=input("                                                                                          => Enter Your Password : ")
    q="select * from auth1"
    cur.execute(q)
    a=cur.fetchone()
    if a[0]==user_id and a[1]==pas :
             print()
             print(" "*84,"⏬ ⤷                                     ⤶ ⏬")
             print(" "*87," ..Log In Successful Please Carry On..")

    else:
       print("no matching")
       menu() #recursion

#============================================================================================

def emptable():
   q="create table employeed(ID int(30),NAME char(30) primary key,POST char(30), SALARY int(30),DOJ date, DOE char(30), ADDRESS char(30))"
   cur.execute(q)
   con.commit()


#============================================================================================

def insert():
    print()
    n=int(input("  => How Many Records Do You Want Yo Insert : "))
    i=0
    while(i<n):
      try:
        print()
        id=int(input("   > Enter Employee ID____  : "))
        name=input("   > Enter Employee Name__  : ")
        post=input("   > Enter Employee Post___ : ")
        sal=int(input("   > Enter Employee Salary : "))
        DOJ=input("   > Enter Date Of Joining  : ")
        DOE=input("   > Enter Date Of Ending_  : ")
        add=input("   > Enter Employee Add. __ : ")
        t=(id,name,post,sal,DOJ,DOE,add,)
        q="insert into employeed values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(q,t)
        con.commit()
        print("     Record insertead")
        i=i+1
      except:
         print("  >>  Please enter a valid value")
  

#============================================================================================

def search():
  print()
  n=int(input("  => How many Time  Do you want to Search Record : "))
  i=0
  while(i<n):
    try:
      print()
      name=input("   > Enter The Name Of Employee : ")
      print(" ","-"*42)
      q="select * from employeed where name=%s"
      t=(name,)
      cur.execute(q,t)
      a=cur.fetchone()
      print()
      print("   > Enter Employee ID____  : ",a[0])
      print("   > Enter Employee Name__  : ",a[1])
      print("   > Enter Employee Post___ : ",a[2])
      print("   > Enter Employee Salary_ : ",a[3])
      print("   > Enter Date Of Joining  : ",a[4])
      print("   > Enter Date Of Ending_  : ",a[5])
      print("   > Enter Employee Add. __ : ",a[6])
      i=i+1
    except:
         print("  >>  Please enter a valid value")

#============================================================================================

def searchA():
       q="select * from employeed"
       cur.execute(q)
       record=cur.fetchall()
       count=1
       for a in record:
         print("\n\n   => Record of",[ count ],"Employee")
         print()
         print("   > Enter Employee ID____  : ",a[0])
         print("   > Enter Employee Name__  : ",a[1])
         print("   > Enter Employee Post___ : ",a[2])
         print("   > Enter Employee Salary_ : ",a[3])
         print("   > Enter Date Of Joining  : ",a[4])
         print("   > Enter Date Of Ending_  : ",a[5])
         print("   > Enter Employee Add. __ : ",a[6])
         count+=1

#============================================================================================

def updatesal():
  print()
  i=0
  while(i<1):
   try:
     n=int(input("  => how many Time  Do you want to Update Salary Record : "))
     for a in range(n):
       try:
         print()
         name=input("   > Enter the Name of Employee whose Salary Do you want to Modify : ")
         sal=int(input("   > Enter Modified Salary : "))
         q="update employeed set SALARY=%s where NAME=%s" #order important
         t=(sal,name)
         cur.execute(q,t)
         con.commit()
         print("     Data Changed")
       except:
          print("  >>  Please enter a valid value")
     i=i+1
   except:
     print("  >>  Please enter a valid value")

#============================================================================================

def updatepost():
  print()
  n=int(input("  => how many Time  Do you want to Update Post Record : "))
  i=0
  while(i<n):
    try:
      print()
      name=input("   > Enter the Name of Employee whose Promoted Do you want to Modify : ")
      pos=input("   > Enter Modified Post : ")
      q="update employeed set POST=%s where NAME=%s" #order important
      t=(pos,name)
      cur.execute(q,t)
      con.commit()
      print("     Data Changed")
      i=i+1
    except:
        print("  >>  Please enter a valid value")

#============================================================================================

def delete():
  print()
  n=int(input("  => How many Time  Do you want to Delete Record : "))
  i=0
  while(i<n):
    try:
      print()
      name=input("   > Enter the name of Employee whose record  do u want to delete : ")
      q="delete from employeed where NAME=%s"
      t=(name,)
      cur.execute(q,t)
      con.commit()
      print("Data Delete")
      i=i+1
    except:
        print("  >>  Please enter a valid value")
   
#============================================================================================

def menu():
  authcheck()
  print()
  print()
  print("="*211)
  print()
  print(" "*86," < ---- EMPLOYEE MANAGEMENT SYSTEM ---- >")
  print()
  print("="*211)
  while True:
    try:
       print()
       print(" ","-"*42)
       print()
       print("  => 1 For Insert New Records : ")
       print("  => 2 For Search One Record : ")
       print("  => 3 For Search All Record : ")
       print("  => 4 For Update Employee Salary : ")
       print("  => 5 For Update Employee Post For Promotion : ")
       print("  => 6 For Delete Employee Record : ")
       print("  => 10 For Exit : ")
       print()
       ch=int(input("  -> Enter Your Choice : "))
       if ch==1:
          insert()
       elif ch==2:
          search()
       elif ch==3:
          searchA()
       elif ch==4:
          updatesal()
       elif ch==5:
          updatepost()
       elif ch==6:
          delete()
       elif ch==10:
          print("Thank You ")
          break
    except:
        print("   >>  Please enter a valid value")



       
