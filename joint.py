a=input('''Enter your choice 
1 for simple calculator
2 for BMI calculator
3 for currency converter
''')
if a == '1':
		print("simple calculator")
		d=input('''press one number 
			1 for add
			2 for subtract 
			3 for multiply 
			4 for divide
			 ''')
		f=int(input("\n\n press enter first number"))
		s=int(input("\n\n press enter second number"))
		fp=open("D:\\New folder\\op.txt","a+")
		fp.write("%s:"%d)
		if d == '1':
			c=f+s
			print (c)
			fp.write("%s:"%c)  
		elif d == '2':
			c=f-s
			print (c) 
			fp.write("%s:"%c)
		elif d == '3':
			c=f*s
			print (c)
			fp.write("%s:"%c)
		elif d == '4':
			c=f/s
			print (c)
			fp.write("%s:"%c)
		else:
			print("invalid input")
			fp.write("\n\n")
			fp.close
elif a == '2':
		print ("BMI calculator")
		n=input("enter user name\n")
		height= float(input("\n\n enter the height in meter"))
		weight=float(input("\n\n enter the weight in kg")) 
		c = weight / (height*height) 
		print ("This  is body mas index:",c)
		fp=open("D:\\New folder\\firsttask.txt","a+")
		fp.write("%s:"%n)
		fp.write("%s:"%c)
		fp.write("\n\n")
		fp.close
else:
	print ("Currency Converter")
	g=input('''press one number 
				1 for us dollar,
				2 for indian rupee
				 ''')
	h=input('''press second number
				1 for us dollar,
				2 for indian rupee
				 ''')
	fp =open("D:\\New folder\\op1.txt","r")    
	if	    g == '1' and h == '2':
					a=float(input("\n\n enter the currency limit "))
					c = fp.readline()
					g = float(c) * a
					print ("INR",g)
	elif    g == '2' and h == '1':
					a=float(input("\n\n enter the currency limit "))
					c = fp.readline()
					g = a / float(c)
					print ("US",g)
	else:
					print ("ok")
					fp.close
		
	