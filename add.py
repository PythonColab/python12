
d=input('''press one number 
1 for add ,
2 for subtract, 
3 for multiply, 
4 for divide
 ''')
a=int(input("\n\n press enter first number"))
b=int(input("\n\n press enter second number"))
fp=open("D:\\New folder\\op.txt","a+")
fp.write("%s:"%d)
if d == '1':
  c=a+b
  print (c)
  fp.write("%s:"%c)  
elif d == '2':
  c=a-b
  print (c) 
  fp.write("%s:"%c)
elif d == '3':
  c=a*b
  print (c)
  fp.write("%s:"%c)
elif d == '4':
  c=a/b
  print (c)
  fp.write("%s:"%c)
else:
  print("invalid input")
fp.write("\n\n")
fp.close
	