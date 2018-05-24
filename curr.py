d=input('''press one number 
1 for us dollar,
2 for indian rupee
 ''')
e=input('''press second number
1 for us dollar,
2 for indian rupee
 ''')
fp=open("D:\\New folder\\op1.txt","r")
if d == '1' and e == '2':
    a=float(input("\n\n enter the currency limit "))
    c = fp.readline()
    g = float(c) * a
    print ("INR",g)
elif d == '2' and e == '1':
    a=float(input("\n\n enter the currency limit "))
    c = fp.readline()
    g = a / float(c)
    print ("US",g)
else:
    print ("ok")
fp.close
  
