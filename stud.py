def nuser ():
    n=input("\nEnter name:")
    phn=input("Enter phone number:")
    uname=input("Enter username:")
    email=input("Enter email:")
    passw1=input("Enter password:")
    passw2=input("Enter password Again:")

    if(passw1==passw2):
        fp=open("D:\\New folder\stud.txt",'w+')
        fp.writelines('\n')
        fp.writelines(n+'\n')
        fp.writelines(phn+'\n')
        fp.writelines(uname+'\n')
        fp.writelines(email+'\n')
        fp.writelines(passw1+'\n')
        fp.writelines('\n')
        fp.close()   
    else:
        print ("you are fill correct detail\n")
        nuser ()
def euser():
    u=input("\nEnter username or email:")
    p=input("\nEnter password:")
    
    fp = open('D:\\New folder\stud.txt')
    lines = fp.read().split("\n") # Create a list containing all lines
    fp.close()
    print(lines)
    i=int(3)
    j=int(5)
    l=0
    #for i in range(0,len(lines)):
    while(i<len(lines)):
        if(u==lines[i] and p==lines[j]):
        print ("you are in student pannel")
            l=0
            break
        
        else:
            l=1
        i=i+7
        j=i+2     
            
        
            
    if l==0:
        print("You Rocked ...")
        print("Sucessfully login.....")
        print("Hello "+lines[i-2]+" How can i help you.....")
    else:
        print("Try again later...")
                    

print("---------------Student Management system-------------------------------")
fp=open("D:\\New folder\\stud.txt","w")
fp.write("--------------student detail\n-----------------")
fp.close()

print("choose option::")

c='Y'
while(c.upper()=='Y'):
    print("\n1.New User\n2.Existing user")
    a=int(input())
    if(a==1):
        #print("Under construction")
        nuser();
        t=input("Do you want to continue(Y/N)")
    elif(a==2):
        #print("Under construction")
        euser()
        t=input("Do you want to continue(Y/N)")
    else:
        print("Wrong choice")
        t=input("Do you want to continue(Y/N)")     