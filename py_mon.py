#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~
#~~~~~~~~~~~~~~~ Coded by Anto Joseph , antojoseph007@gmail.com ~~~~^~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~
import hashlib
import smtplib

# function takes input the filename , website name and its predef hash sum 
def findsum(filename,name,hashsum):
    md5 = hashlib.md5()
    try :
        f =  open(filename,'rb')
        chunk = f.read()
        f.close()
        x= hashlib.sha256(chunk).hexdigest() 
        compare(x,hashsum,name)
    except IOError as e:
         print e
         panic()

# function compares the actual sha1 sum with the pre def sum , calls panic if changed
def compare (predef_hash,hashsum,name):
    if(predef_hash==hashsum):
        print "Hash Matches for {0}".format(name)
    else:
        print "Hash Failed for {0}".format(name)
        panic()
          

# Sends an email notification to the admin 
def panic():
    message = """From: From Person <hashverification@orangeserver.com>
    To: To Person <anto@codelattice.com>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: Hash Verification failed 

    <b>Either the file is missing or file has been altered !</b>
    <h1>Panic !!!</h1>
    """
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"
 
 
 
# put your  sha256 hash codes in here
hash1="991699c452c56d75e18a8a9d6654f2b39c6fbbbd98c94d8c76d953d3d8cde5c5"
hash2="7c0f08c36cfee8a25d0c87e435e507f302cb48b41d2a9adcdac87498773ff16f"
hash3="a2d49340e7eb2e3afd3d3da378d7c40b926228c45dcc93e10b8f2eaf8d8bad65"
 
 
 #put your files , a name and their hash reference here 
findsum("images.jpg","mywebsite",hash1)
findsum("01.jpg","mysecondwebsite",hash2)
findsum("tlogo2.jpg","4rdwebsite",hash3)


