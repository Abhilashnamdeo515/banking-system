import mysql.connector

import admin,user

con=mysql.connector.connect(host="localhost",user="root",
                           passwd="Abhi@4321")

cur=con.cursor()



def panel():
    print()
    print(" "*75," { : => WELCOME TO EMPLOYEE MANAGMENT PANNEL SECTION <= : }")
    print(" "*70,"="*70)
    print()
    print(" "*88," ➟  Select ' 1 ' For Admin Panel   ")
    while True:
      try:
       print()
       print("                                                                                                        ⌨  ")
       ch=int(input("                                                                                                Enter Your Choice : "))
       if ch==1:
         admin.menu()
       elif ch==10:
          break
       else:
          print("invalid value !!!!")
      except:
         print("please enter valid value")

panel()

    










    






