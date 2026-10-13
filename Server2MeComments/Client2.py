import json
import os
import io
import hmac
import hashlib
import requests
import math 
import subprocess
import string
import sys
#import sumpiesh


headers = {'Content-type': 'application/json'}

param_list=[]
info={  
"encoded_file": "",
"compression_algorithm": "arithmetic",
"encoding": "linear",
"parameters":[param_list],
"errors": "",
"SHA256": "",
"entropy":""
}


#Εδώ βάζουμε το όνομα του αρχείου που θέλουμε να χρησιμοποιήσουμε
print("Enter the text file name:")
txtfile= "DYamiBaraLyrics.txt"#input()


#---Εικόνα---
'''
subprocess.call(['python', 'sumpiesh\\map_wencode.py'])

f = open('sumpiesh\\tag_ls2','rb')
bin = f.read()
f.close()
hex_bin=bin.hex()
'''

#ανοίγω και διαβάζω την εικόνα, την μετατρέπω σε 16ικο και τη βάζω στο dictionary

with open(txtfile, 'r') as file:
    file_content = file.read()

#print(file_content)

'''
file = open(txtfile,'r')
bin = file.read()
file.close()
#hex_bin=bin.hex()

lines =words = chars = spaces = 0

with open(file, "r") as f:
    for x in f:
        lines += 1
        words += len(x.split())
        spaces += x.count(" ")
        chars += sum(1 for c in x if c not in (" ", "\n"))

print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
print("Spaces:", spaces)

entropy = 0
for x in range(chars):
    p_x = float(data.count(chr(x)))/len(data)
    if p_x > 0:
      entropy += - p_x*math.log(p_x, 2)
print(entropy)
'''


#info["encoded_image"]= hex_bin

#---Αλγόριθμος συμπίεσης---
print(f"Compression Algorithm:{info['compression_algorithm']}")

#---Encoding---
print(f"Encoding:{info['encoding']}")

#---Λίστα παραμέτρων---
'''
print("Enter the parameters")
text=input()
while (text!="end"):
    
    if(text!="end"):
        param_list.append(text)
    text=input()
'''

#param_list.append()

'''
def arxeia(file):
    f = open(file,'rb')
    bin = f.read()
    f.close()
    hex_bin=bin.hex()
    param_list.append(hex_bin)

arxeia("sumpiesh\\arithmos_bit2")
arxeia("sumpiesh\\noumero2")
arxeia("sumpiesh\\diafora2")
arxeia("sumpiesh\\ls_pososta_ls2")
arxeia("sumpiesh\\ls_xarakthres_ls2")
#arxeia("sumpiesh\\arithmos_bit2")
        
#print(f"Parameter List:{param_list}")
print("parameters imported")
'''

#---Errors---
print("Errors (0-100):")
info["errors"]= "2" #input()
print(info["errors"])


#---SHA256---

#string = file_content.encode()

# Initializing the sha256() method
#sha256 = hashlib.sha256()

# Passing the byte stream as an argument
#sha256.update(string)
#hex_digest = sha256.hexdigest()

#string = b'gamw to xristo mou gamw'
#hash_object = hashlib.sha256(string)

#bytefile= file_content.encode
#print(hash_object)

#ta prwta lines
#hash_object = hashlib.sha256(file_content.encode())
#hex_digest = hash_object.hexdigest()

hash_func = hashlib.new('sha256')
    
with open(txtfile, 'rb') as file:
        # Read the file in chunks of 8192 bytes
        chunksize= 1024 #de douleuei kala oute me 8192, vgazei to idio idk 
        while True:
            chunk = file.read(chunksize)
            #chunk=chunk.decode()
            #chunk=chunk.replace("\n", " ").replace("\r", "")
        
            print(chunk)
            #chunk+=chunk
            #print("deutero print")
            #print(chunk)

            if not chunk:
                 break
            #print(chunk)
            
            #chunk=chunk.encode()
            hash_func.update(chunk)
            #print(chunk)
            #hash_func.hexdigest()
            #print(hash_func.hexdigest)
            #hash_func=hashlib.sha256(chunk)
#print(hash_func)
#print(chunk)
hex_digest=hash_func.hexdigest()

'''
hash_func = hashlib.new('sha256')
    
with open(txtfile, 'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hash_func.update(chunk)
    
hex_digest=hash_func.hexdigest()

#to panw kai katw dinoun to idio hash pou einai pali lathos

with open(txtfile,"rb") as f:
    bytes = f.read() # read entire file as bytes
    hex_digest = hashlib.sha256(bytes).hexdigest();
    #print(readable_hash)
'''

'''
#den anagnwrizei to file_digest san entolh for some reason
with open(txtfile, "rb") as f:
    digest = hashlib.file_digest(f, "sha256")

hex_digest=digest.hexdigest()
'''

info["SHA256"]=hex_digest
print(f"SHA256:{hex_digest}")


#---Εντροπία---

def entropy_finder(data):
     if not data:
          print("de douleuw pali")
          return 0
     entropy=0
     for x in string.printable:
        p_x = float(data.count(x))/len(data)
        if p_x > 0:
             entropy += - p_x*math.log(p_x, 2)
     return(entropy)   


Text_entropy= entropy_finder(file_content)     
info["entropy"]=Text_entropy
print(f"entropy:{Text_entropy}")


#βάζω τα στοιχεία του dictionary σε ενα καινούριο json
("info.json", {})

with open("info.json", "w") as f:
        json.dump(info, f, indent=4)

#print(info["compression_algorithm"])


#response = requests.post(url="http://192.168.2.8:5000/", json=info , headers=headers)
response = requests.post(url="http://127.0.0.1:5000/", json=info , headers=headers)

print(response.text)

