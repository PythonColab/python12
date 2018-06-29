# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 17:08:48 2018

@author: SURAJ


"""
# import file part
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")
import pymysql
db=pymysql.connect("localhost","root","","pro")
cursor=db.cursor()


import time





#existing admin pannel
def eadm():
    auser=input("Enter admin username\n")
    apsd=input("Enetr password\n")
    sql="select pass from admin where uname='%s'" %auser
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        cd = row[0]    
        if(apsd==cd):
            while(apsd==cd):
                 print("welcome admin, In Library mangment\n")
                 afac=input("""hello,please choose action
                          1 for add book
                          2 for show book detail
                          3 for remove book
                          4 for check bill status
                          5 for update book
                          6 for update admin detail
                          7 for remove student detail
                          8 for show admin detail
                          9 for change bill status 
                          """)
                 if(afac=='1'):
                      print("hello admin, add your book\n")
                      ab=input("enter book tittle\n")
                      b=input("enter book author name\n")
                      c=input("enter book publiction name\n")
                      d=input("enter book pub year\n")
                      e=input("enter book related subject\n")
                      f=input("enter book number of books\n")
                      g=input("enter book price of books\n")
                      cursor.execute("""
                                   insert into book(btittle, aname, pname, pyear,rsub,no,price) VALUES
                                   (%s,%s,%s,%s,%s,%s,%s)""" ,(ab,b, c, d, e, f, g))
                      db.commit()
                      sel="select id from book"
                      a=cursor.execute(sel)
                      print("your Book id is:", a)
                 elif(afac=='2'):
                     print("hello student, show your book\n")
                     al=input("what is your choice show all or one book\n")
                     if(al=="one"):
                         b=input("enter your book tittle\n")
                         sql="select * from book where btittle='%s'" %b
                         cursor.execute(sql)
                         results = cursor.fetchall()
                         for row in results:
                             bid = row[0]
                             btittle = row[1]
                             aname = row[2]
                             pname = row[3]
                             pyear = row[4]
                             rsub = row[5]
                             no = row[6]
                             price = row[7]
                             print("book id" , bid)  
                             print("book tittle:",btittle)
                             print("author name:",aname)
                             print("publisher name:",pname) 
                             print("publication year:" ,pyear)
                             print("related sub:" ,rsub)
                             print("number of books:" ,no)
                             print("price of books:" ,price)
                         
                     else:
                         print("hello admin, books in library\n")
                         se="select * from book"
                         cursor.execute(se)
                         print("All books")
                         nresults = cursor.fetchall()
                         for row in nresults:
                             bid = row[0]
                             btittle = row[1]
                             aname = row[2]
                             pname = row[3]
                             pyear = row[4]
                             rsub = row[5]
                             no = row[6]
                             price = row[7]
                             print("book id" , bid)  
                             print("book tittle:",btittle)
                             print("author name:",aname)
                             print("publisher name:",pname) 
                             print("publication year:" ,pyear)
                             print("related sub:" ,rsub)
                             print("number of books:" ,no)
                             print("price of books:" ,price)
                             
                 elif(afac=='3'):
                     print("hello admin, remove your book\n")
                     b=int(input("enter book id"))
                     sql="delete from book where id='%s'" % b
                     cursor.execute(sql)
                     db.commit()
                 elif(afac=='4'):
                     print("hello admin, check bill status\n")
                     bill();
                 elif(afac=='5'):
                     print("please fill correct details\n")
                     uab=input("enter book tittle\n")
                     ub=input("enter book author name\n")
                     uc=input("enter book publiction name\n")
                     ud=input("enter book pub year\n")
                     ue=input("enter book related subject\n")
                     uf=input("enter book number of books\n")
                     ug=input("enter book price of books\n")
                     exid=int(input("Enter Update book id"))
                     cursor.execute ("""
                                        UPDATE  book
                                        SET btittle=%s, aname=%s, pname=%s, pyear=%s, rsub=%s, no=%s, price=%s
                                        WHERE id=%s
                                        """, (uab, ub, uc, ud, ue, uf, ug, exid))
                     db.commit()
                 elif(afac=='6'):
                      cursor.execute("select name, uname, pass from admin where uname='%s'" % auser)
                      result=cursor.fetchall()
                      for row in result:
                          aname = row[0]
                          auname = row[1]
                          apass = row[2]
                      w=input("aap update kya krna chate hain\n ")
                      if(w=="name"):
                                print("Old Name Is:" , aname)
                                nn=input("Enter New Name\n")
                                cursor.execute("update admin set name=%s where uname=%s" , (nn ,auser))
                                db.commit()
                                print("Your new name is::" , nn)
                      elif(w=="username"):
                                print("Old User Name Is:" , auname)
                                nn=input("Enter New User Name\n")
                                cursor.execute("update admin set uname=%s where uname=%s" , (nn ,auser))
                                db.commit()
                                print("Your new user name is::" , nn)
                      elif(w=="password"):
                                print("Old Password Is:" , apass)
                                nn=input("Enter New Password\n")
                                cursor.execute("update admin set pass=%s where uname=%s" , (nn ,auser))
                                db.commit()
                                print("Your new password is::" , nn)
                      else:
                                print("This field is not avilable\n")
    
                 elif(afac=='7'):
                      print("Please remove student\n")
                      rs=int(input("Enter Student ID\n"))
                      cursor.execute("delete from student where id=%s"  % rs)
                      db.commit()
                      
                 elif(afac=='8'):
                      print("hello admin,show detail\n")
                      cursor.execute("""select * from admin where uname='%s'""" % auser)
                      eresult=cursor.fetchall()
                      for row in eresult:
                          eide = row[0]
                          ename = row[1]
                          euname = row[2]
                          passw = row[3]
                      print("Your Id is" , eide)
                      print("Your Name is" , ename)
                      print("Your User Name is" , euname)
                      print("Your password is" , passw)
                 elif(afac=='9'):
                     bp=input("Enter Bill Holder Name \n")
                     cursor.execute("select * from bill where sname='%s'" % bp)
                     presult=cursor.fetchall()
                     for row in presult:
                         bid = row[0]
                         psname = row[1]
                         pbtittle = row[2]
                         date = row[3]
                         tfare = row[4]
                         paid = row[5]
                         print("your bill id:",bid)
                         print("your name:",psname)
                         print("your book tittle:",pbtittle)
                         print("your issue date:",date)
                         print("your total fare:",tfare)
                         print("your status:", paid)
                     pri=input("Are you  confirm this bill is paid\n")    
                     if(pri=="yes" or "YES"):
                         psql="""update bill set status="Paid" where sname='%s'""" % bp 
                         cursor.execute(psql)
                         db.commit()
                         print("This bill is paid\n")
                     else:
                         print("Ok this bill is not paid\n")
                 else:
                     print("please fill correct choice")
                 du=input("do you want LOGOUT\n")
                 if(du=="yes"):
                     break
                 else:
                     continue                
        else:
                print("invalid username or password\n")
                nadm();
          








# new admin pannel
def nadm():
    admin=input("are you existing yes or no\n")
    if(admin=="no"):
        print("Please Fill Enroll Detail\n")
        aa=input("Enter Your Name\n")
        bb=input("Enter Your UserName\n")
        cc=input("Enter Your Password\n")
        cursor.execute("""insert into admin(name,uname,pass) values(%s,%s,%s)""",(aa,bb,cc))
        db.commit()
        sel="select id from admin"
        a=cursor.execute(sel)
        print("your admin id is:" , a)
        ead=input("do you want continue y or n\n")
        if(ead=='y' or 'Y'):
            eadm();
        else:
            print("ok , thanks.")
    elif(admin=="yes" or "YES"):
        eadm();
    else:
        print("Please  give answer in yes or no\n")



#bill pannel
def bill():
    name=input("Enter bill holder name\n")
    cursor.execute("select * from bill where sname='%s'" % name)
    presult=cursor.fetchall()
    for row in presult:
        bid = row[0]
        psname = row[1]
        pbtittle = row[2]
        date = row[3]
        tfare = row[4]
        paid = row[5]
        if(name==psname):
            print("your bill id:",bid)
            print("your name:",psname)
            print("your book tittle:",pbtittle)
            print("your issue date:",date)
            print("your total fare:",tfare)
            print("your status:", paid)
            print(" NOTE :: Please Reamember Your bill id for return book\n")
            print(" NOTE :: This rate is include with service and GST managment\n")
            
        else:
            print("please try again\n")




# return pannel
def retur():
    noo=input("Enter bill holder id\n")
    da=int(input("Enter keep days\n"))
    cursor.execute("select * from bill where bid='%s'" % noo)
    bresult=cursor.fetchall()
    for row in bresult:
        bid = row[0]
        psname = row[1]
        pbtittle = row[2]
        date = row[3]
        tfare = row[4]
        paid = row[5]
        if(da > 7):
            do = da - 7
            du = do * 10 
            tfa= tfare + du
            cursor.execute("update bill set tfare=%s where bid=%s" , (tfa ,noo))
            db.commit()
            print("your bill id:",bid)
            print("your name:",psname)
            print("your book tittle:",pbtittle)
            print("your issue date:",date)
            print("your total fare:",tfa)
            print("bill satus" , paid)
            print(" NOTE :: Please Reamember Your bill id for return book\n")
            print(" NOTE :: This rate is include with service and GST managment\n")
        else:   
            print("your bill id:",bid)
            print("your name:",psname)
            print("your book tittle:",pbtittle)
            print("your issue date:",date)
            print("your total fare:",tfare)
            print("bill satus" , paid)
            print(" NOTE :: Please Reamember Your bill id for return book\n")
            print(" NOTE :: This rate is include with service and GST managment\n")







# book issue pannel
def issue():
    iss=input("Enter Book Tittle\n")
    cursor.execute("select btittle,price from book where btittle='%s'" % iss)
    result = cursor.fetchall()
    for row in result:
        btittle = row[0]
        price = row[1]
    print("book tittle:",btittle)
    print("book price:",price)
    issue=input("Are you confirm for issue then press i for bill\n")
    if(issue=='i'):
        sname=input("Enter bill holder name\n")
        dat = time.asctime( time.localtime(time.time()) )
        cursor.execute("select btittle ,price from book where btittle='%s'" % iss)
        bresult = cursor.fetchall()
        for row in bresult:
            btittle = row[0]
            price = row[1]
        d=price + 20 + 20    
        cursor.execute("""insert into bill(sname,btittle,date,tfare) values(%s,%s,%s,%s)""",(sname,btittle,dat,d))
        db.commit()
        print("your book is issued\n")
        pbill=input("press  p print your bill\n")
        if(pbill=='p'):
            bill();
            
        else:
            print("your book is issued\n")
    else:
         estu();
         print("Thank you come again\n")
   
        





# existing student pannel
def estu():
    user=input("Enter Your UserName\n")
    pasd=input("Enter Your Password\n")
    sql="select pass from student where uname='%s'" %user
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        cd = row[0]
        if(pasd==cd):
            while(pasd==cd):
                print("welcome in Library mangment\n")
                fac=input("""hello,please choose action
                          1 for view student detail
                          2 for search book
                          3 for issue book
                          4 for return book
                          5 for update student detail
                          6 for Check bill status
                          """)
                if(fac=='1'):
                    sql="select * from student where uname='%s'" % user 
                    cursor.execute(sql)
                    result=cursor.fetchall()
                    for row in result:
                        ide = row[0]
                        name = row[1]
                        fname = row[2]
                        uname = row[3]
                        course = row[4]
                        branch= row[5]
                        year = row[6]
                        pasd = row[7]
                    print("Your Id is::" , ide)
                    print("Your Name is::" , name)
                    print("Your Father'sName is:: MR. " , fname)
                    print("Your UserName is::" , uname)
                    print("Your Course is::" , course)
                    print("Your Branch is::" , branch)
                    print("Your Year is::" , year)
                    print("Your pasd is::" , pasd)
                elif(fac=='2'):
                     print("hello student, Search your book\n")
                     sur=input("enter related subject of books\n")
                     sql="select btittle,aname,pname,rsub,price from book where rsub='%s'" %sur  
                     cursor.execute(sql)
                     results = cursor.fetchall()
                     for row in results:
                         btittle = row[0]
                         aname = row[1]
                         pname = row[2]
                         rsub = row[3]
                         price = row[4]
                         if(sur==rsub):
                             print("book tittle:",btittle)
                             print("author name:",aname)
                             print("publisher name:",pname) 
                             print("related sub:" ,rsub)
                             print("book price:" ,price)
                             awq=input("are you sure for issue this book\n")
                             if(awq=="yes"):
                                 issue();
                             else:
                                 print("please Reconfirm your books\n")
                         else:
                             print("This subject is not avilable\n")
                elif(fac=='3'):
                    issue();
                elif(fac=='4'):
                    retur();
                elif(fac=='5'):
                     print("Please Fill Enroll Detail\n")
                     a=input("Enter Your Name\n")
                     b=input("Enter Your Father Name\n")
                     c=input("Enter Your UserName\n")
                     d=input("Enter Your Course\n")
                     e=input("Enter Your Branch\n")
                     f=input("Enter Your Year\n")
                     g=input("Enter Your Password\n")
                     esid=int(input("Enter your id\n"))
                     cursor.execute ("""
                                       UPDATE  student
                                       SET name=%s, fname=%s, uname=%s, course=%s, branch=%s, year=%s, pass=%s 
                                       WHERE id=%s
                                    """, (a, b, c, d, e,f, g, esid))
                     db.commit()
                elif(fac=='6'):
                    ide=int(input("Enter bill holder ID\n"))
                    cursor.execute("select bid ,tfare, status from bill where bid=%d" % ide )
                    presult=cursor.fetchall()
                    for row in presult:
                        bid = row[0]
                        price = row[1]
                        paid = row[2]
                        if(ide==bid):
                            print("your bill id:",bid)
                            print("Your bill id:" , price)
                            print("your status:", paid)
                            print("For Any Help Contact Librian\n")
                            
                        else:
                            print("please try again\n")
                    
                else:
                    print("Please choose correctly")
                du=input("do you want LOGOUT\n")
                if(du=="yes"):
                    break
                else:
                    continue            
        else:
            print("Invalid Username OR Password\n")
            stu();





# new student pannel
def stu():
    print("WELCOME IN STUDENT PANNEL\n")
    af=input("ARE YOU EXISTING \n")
    if(af=="yes"):
        estu();
    else:
        print("Please Fill Enroll Detail\n")
        a=input("Enter Your Name\n")
        b=input("Enter Your Father Name\n")
        c=input("Enter Your UserName\n")
        d=input("Enter Your Course\n")
        e=input("Enter Your Branch\n")
        f=input("Enter Your Year\n")
        g=input("Enter Your Password\n")
        cursor.execute("""insert into student(name,fname,uname,course,branch,year,pass) values(%s,%s,%s,%s,%s,%s,%s)""",(a,b,c,d,e,f,g))
        db.commit()
        sql="select id from student"
        ad=cursor.execute(sql)
        print("Your ID is:::" , ad)
        r=input("Do you want continue yes or no")
        if(r=="yes"):
            estu();
        else:
            print("Thank You For Enroll an user")        






# main programe
choice=input("are you student or admin\n")
if(choice=="admin"):
    nadm();
elif(choice=="student"):
    stu();
else:
    print("THIS PANNEL IS NOT AVILABLE")
            
    
    
       

db.close()
    
                         
    


