#!/usr/bin/python3.2
import sys
import hashlib
class hashguru:
    def print_banner(self):
        print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print ("       Hackproofme by ANTO !              ")
        print ("__________________________________________")
        print ("******************************************")
        print ("")
        print ("syntax  ./hasher.py filename")

    def hashit(self,filename):
        try :
            self.filename =filename
            f =  open(filename,'rb')
            chunk = f.read()
            f.close()
            x= hashlib.sha256(chunk).hexdigest() 
            print("")
            print("")
            print("Sha 256 hash for the file {0} is : {1} ".format(filename,x))
            return x
        except IOError as e:
            print (e)
            
    
    
    

         
