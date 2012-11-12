#!/usr/bin/python3.2

from myclass import *
from hasher import *

hashme= hashguru()
x=dbhandler("adadada")
x.mkdb()


# Checking if argument was provided


if (len(sys.argv)<=1):
    hashme.print_banner()
    print ("Error ! No filename specified ")
elif(sys.argv[1]=="-check"):
		x.checkhash()
elif(sys.argv[1]=="-show"):
		x.show()
else:
    hashme.print_banner()     
    hashsum = hashme.hashit(sys.argv[1])
    x.insert(sys.argv[1],hashsum)


