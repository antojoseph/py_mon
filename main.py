#!/usr/bin/python3.2

from myclass import *
from hasher import *


hashme= hashguru()
x=dbhandler("adadada")
x.mkdb()


def show():	
	print ("")
	print ("Printing Contents of the DB !")    
	print ("")
	result = x.show()
	for row in result:
		print(row[0],row[1],row[2])
	print ("")
	print ("")




def checkhash():
	result=x.show()
	for row in result:
		sum_now= hashme.hashit(row[1])
		if (sum_now == row[2]):
			print("file is not changed ")
		else:
			print("file has changed ")

# Checking if argument was provided


if (len(sys.argv)<=1):
    hashme.print_banner()
    print ("Error ! No filename specified ")
elif(sys.argv[1]=="-check"):
		checkhash()
elif(sys.argv[1]=="-show"):
		show()
else:
    try:
    	hashme.print_banner()
    	f =  open(sys.argv[1],'rb')
    	f.close()        
    	hashsum = hashme.hashit(sys.argv[1])
    	x.insert(sys.argv[1],hashsum)
    except:
    	print("File Doesn't Exist or You don't have Sufficent Privilages !")

